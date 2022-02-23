import os
from pathlib import Path
import shutil
import time
from .filemanager_driver import FileManagerDriver


class LocalDriver(FileManagerDriver):
    def _get_path(self, extra=None) -> str:
        """Get the path to the filemanager directory"""

        request = self.application.make("request")
        folder = request.input("folder", None)

        path = self.root_path
        if folder:
            folders = folder.split(",")
            path = os.path.join(self.root_path, *folders)

        if extra:
            path = os.path.join(path, extra)

        return path

    def total_size(self):
        """Get the total size of the filemanager directory"""

        size = sum(file.stat().st_size for file in Path(self.root_path).rglob("*"))
        return self.convert_bytes(size)

    def exists(self, name) -> bool:
        """Check if a file/path exists in the filemanager directory"""

        return os.path.exists(self._get_path(name))

    def upload(self, file):
        """Upload a file to the filemanager directory"""

        request = self.application.make("request")
        folder = request.input("folder", None)
        path = "filemanager"

        if folder:
            path = "filemanager/{}".format(folder.replace(",", "/"))

        self.storage.disk("local").put_file(path, file)

    def create_folder(self, name) -> bool:
        """Create a folder in the filemanager directory"""

        try:
            path = self._get_path(name)
            if not self.exists(path):
                os.mkdir(self._get_path(name))
                return True
        except Exception as e:
            print(e)
        return False

    def rename(self, path, name) -> bool:
        """Rename a file/folder in the filemanager directory"""

        if os.path.exists(path):
            # check if path is file
            if os.path.isfile(path):
                name = "{name}.{ext}".format(name=name, ext=path.split(".")[-1])
            os.rename(path, self._get_path(name))
            return True
        return False

    def delete_folder(self, path) -> bool:
        """Delete a folder in the filemanager directory"""

        try:
            if os.path.exists(path):
                if len(os.listdir(path)) > 0:
                    shutil.rmtree(path)
                else:
                    os.rmdir(path)
                return True
        except Exception as e:
            print(e)
        return False

    def all_files(self):
        data = {
            "folders": [],
            "files": [],
            "total_size": self.total_size(),
        }

        path = self._get_path()

        with os.scandir(path) as entries:
            for item in entries:
                name = item.name
                byte_size = (
                    item.stat().st_size
                    if item.is_file()
                    else sum(file.stat().st_size for file in Path(item.path).rglob("*"))
                )
                size = self.convert_bytes(byte_size)
                created_at = time.ctime(item.stat().st_ctime)
                modified_at = time.ctime(item.stat().st_mtime)

                file_url = item.path.replace(self.root_path, "/filemanager-uploads")
                file_url = file_url.replace("\\", "/")

                file_item = {
                    "name": name if item.is_dir() else item.name.split(".")[0],
                    "size": size,
                    "created": created_at,
                    "modified": modified_at,
                    "path": item.path,
                }

                if item.is_dir():
                    file_item["total_files"] = len(os.listdir(item.path))
                    data.get("folders").append(file_item)
                else:
                    file_item["url"] = file_url
                    file_item["mime"] = self._get_media_type(item)
                    data.get("files").append(file_item)

        return self.validate(data)
