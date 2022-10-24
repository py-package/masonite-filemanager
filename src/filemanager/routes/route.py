from masonite.routes import Route
from masonite.configuration import config
from src.filemanager.controllers.filemanager_controller import FileManagerController

middleware = config('filemanager.middleware')

ROUTES = Route.group(
    [
        Route.get("", FileManagerController.index).name("ui"),
        Route.post("", FileManagerController.upload).name("store"),
        Route.get("/all-files", FileManagerController.all_files).name("list"),
        Route.post("/rename", FileManagerController.rename).name("rename"),
        Route.post("/create-folder", FileManagerController.create_folder).name("create_folder"),
        Route.post("/delete-folder", FileManagerController.delete_folder).name("delete_folder"),
        Route.post("/delete-file", FileManagerController.delete_file).name("delete_file"),
        Route.get("/picker", FileManagerController.picker).name("picker"),
    ],
    prefix="/filemanager",
    middleware=middleware,
    name="filemanager."
)
