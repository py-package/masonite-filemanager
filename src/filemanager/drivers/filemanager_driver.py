import mimetypes
import os
from ..constants import NOT_IMPLEMENTED_MSG


class FileManagerDriver:
    def __init__(self) -> None:
        from wsgi import application

        self.application = application
        self.storage = application.make("storage")
        self.root = self.storage.disk("local")
        self.root_path = self.root.get_path("filemanager")

        if not os.path.exists(self.root_path):
            os.mkdir(self.root_path)

    def _get_path(self, extra=None) -> str:
        raise NotImplementedError(NOT_IMPLEMENTED_MSG)

    def _get_media_type(self, file) -> str:
        return mimetypes.guess_type(file.name)[0]

    def total_size(self) -> str:
        raise NotImplementedError(NOT_IMPLEMENTED_MSG)

    def upload(self, file):
        raise NotImplementedError(NOT_IMPLEMENTED_MSG)

    def rename(self, path, name) -> bool:
        raise NotImplementedError(NOT_IMPLEMENTED_MSG)

    def all_files(self) -> dict:
        raise NotImplementedError(NOT_IMPLEMENTED_MSG)

    def exists(self, name) -> bool:
        raise NotImplementedError(NOT_IMPLEMENTED_MSG)

    def create_folder(self, name) -> bool:
        raise NotImplementedError(NOT_IMPLEMENTED_MSG)

    def delete_folder(self, name) -> bool:
        raise NotImplementedError(NOT_IMPLEMENTED_MSG)

    def delete_file(self, name) -> bool:
        raise NotImplementedError("Not implemented")

    def convert_bytes(self, num) -> str:
        """
        this function will convert bytes to MB.... GB... etc
        """
        step_unit = 1000.0  # 1024 bad the size

        for x in ["bytes", "KB", "MB", "GB", "TB"]:
            if num < step_unit:
                return "%3.1f %s" % (num, x)
            num /= step_unit

    def validate(self, data: dict) -> dict:
        try:
            if data.get("total_size") is None:
                raise ValueError("total_size key is required")

            if data.get("folders") is None:
                raise ValueError("folders key is required")

            if data.get("files") is None:
                raise ValueError("files key is required")

            data["folders"] = self.verify_folder_data(data["folders"])
            data["files"] = self.verify_file_data(data["files"])

            return data

        except Exception as e:
            raise ValueError(e)

    def verify_folder_data(self, folders: list) -> list:
        try:
            filtered_folders = []

            for folder in folders:
                if all(
                    key in folder
                    for key in ["name", "size", "path", "created", "modified", "total_files"]
                ):
                    filtered_folders.append(folder)

            return filtered_folders

        except Exception as e:
            raise ValueError(e)

    def verify_file_data(self, files: list) -> list:
        try:
            filtered_files = []

            for file in files:
                if all(
                    key in file
                    for key in ["name", "size", "path", "created", "modified", "url", "mime"]
                ):
                    filtered_files.append(file)
            return filtered_files

        except Exception as e:
            raise ValueError(e)
