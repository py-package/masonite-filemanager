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
        Route.post("/filemanager/move-file", FileManagerController.move_file),
        Route.post("/filemanager/file-info", FileManagerController.file_info),
        Route.post("/filemanager/get-preview", FileManagerController.get_preview),
        Route.post("/filemanager/delete-file", FileManagerController.delete_file),
        Route.get("/filemanager/picker", FileManagerController.picker),
    ]
)
