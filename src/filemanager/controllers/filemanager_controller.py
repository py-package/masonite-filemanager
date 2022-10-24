from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masonite.views import View
from masonite.configuration import config
from ..filemanager import FileManager
import json


class FileManagerController(Controller):
    def __init__(self, response: Response, request: Request) -> None:
        self.response = response
        self.request = request
        self.manager = FileManager()

    def index(self, view: View):
        return view.render("filemanager:index", {})

    def file_info(self):
        file = self.request.input("file")
        return self.manager.provider().file_info(file)

    def all_files(self):
        query = self.request.input("query", "")
        if query:
            return self.manager.provider().search_files(query=query)
        return self.manager.provider().all_files()

    def upload(self):
        files = self.request.input("files")
        self.manager.provider().upload(files)

        if config("filemanager.generate_previews"):
            self.manager.provider().generate_previews(files)

        return self.response.json(
            {
                "message": "File uploaded!",
            }
        )

    def get_preview(self, view: View):
        file = json.loads(self.request.input("file"))
        ext = file["extension"][1:]
        mime, type = file["mime"].split("/")
        if mime == "image":
            return {
                "html": view.render(
                    "filemanager:partials.previews.image", {"file": file, "type": ext}
                ).rendered_template
            }
        elif mime == "audio":
            return {
                "html": view.render(
                    "filemanager:partials.previews.audio", {"file": file, "type": ext}
                ).rendered_template
            }
        elif mime == "video":
            return {
                "html": view.render(
                    "filemanager:partials.previews.video", {"file": file, "type": ext}
                ).rendered_template
            }
        elif mime == "application":
            if type == "pdf":
                return {
                    "html": view.render(
                        "filemanager:partials.previews.pdf", {"file": file}
                    ).rendered_template
                }
        return {
            "html": view.render(
                "filemanager:partials.previews.file", {"file": file, "type": ext}
            ).rendered_template
        }

    def rename(self):
        name = self.request.input("name")
        path = self.request.input("path")
        self.manager.provider().rename(path, name)

        return self.response.json(
            {
                "message": "File/Folder renamed!",
            }
        )

    def create_folder(self):
        name = self.request.input("name")

        if not self.manager.provider().exists(name):
            self.manager.provider().create_folder(name)

            return self.response.json(
                {
                    "message": "Folder Created...",
                }
            )

        return self.response.json(
            {
                "message": "Folder already exists!",
            }
        )

    def delete_folder(self):
        path = self.request.input("path")

        try:
            self.manager.provider().delete_folder(path)

            return self.response.json(
                {
                    "message": "Folder deleted...",
                }
            )
        except Exception as e:
            print(e)

        return self.response.json(
            {
                "message": "Folder doesn't exists!",
            }
        )

    def move_file(self):
        paths = json.loads(self.request.input("paths"))
        errors = []
        for path in paths:
            try:
                self.manager.provider().move_file(path["from"], path["to"])
            except Exception:
                return {
                    "message": "Files don't" if len(errors) > 1 else "File doesn't" + " exist!",
                    "failed": errors,
                }

        return {"message": "Files" if len(errors) > 1 else "File" + " moved!"}

    def delete_file(self):
        path = self.request.input("path")
        try:
            self.manager.provider().delete_file(path)
            return self.response.json(
                {
                    "message": "File deleted...",
                }
            )
        except Exception as e:
            print(e)

        return self.response.json(
            {
                "message": "File doesn't exists!",
            }
        )

    def picker(self, view: View):
        return view.render("filemanager:picker", {})
