from masonite.routes import Route

from ..controllers.filemanager_controller import FileManagerController


ROUTES = Route.group(
    [
        Route.get("/filemanager", FileManagerController.index),
        Route.post("/filemanager", FileManagerController.upload),
        Route.get("/filemanager/all-files", FileManagerController.all_files),
        Route.post("/filemanager/rename", FileManagerController.rename),
        Route.post("/filemanager/create-folder", FileManagerController.create_folder),
        Route.post("/filemanager/delete-folder", FileManagerController.delete_folder),
        Route.post("/filemanager/delete-file", FileManagerController.delete_file),
    ]
)
