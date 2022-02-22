from masonite.controllers import Controller
from masonite.request import Request
from masonite.request import Request
from masonite.response import Response
from masonite.views import View
from ..filemanager import FileManager


class FileManagerController(Controller):
    
    def __init__(self, response: Response, request: Request) -> None:
        self.response = response
        self.request = request
        self.manager = FileManager()
    
    def index(self, view: View):
        return view.render('filemanager:index', {})
        
    def all_files(self):
        return self.manager.provider().all_files()
    
    def upload(self):
        file = self.request.input('file')
        self.filemanager.upload(file)
        
        return self.response.json({
            "message": "File uploaded!",
        })
    
    def rename(self):
        name = self.request.input('name')
        path = self.request.input('path')
        self.filemanager.rename(path, name)
        
        return self.response.json({
            "message": "File/Folder renamed!",
        })
    
    def create_folder(self):
        name = self.request.input('name')
        
        if not self.filemanager.exists(name):
            self.filemanager.create_folder(name)
            
            return self.response.json({
                "message": 'Folder Created...',
            })
            
        return self.response.json({
            "message": "Folder already exists!",
        })
    
    def delete_folder(self):
        path = self.request.input('path')
        
        try:
            self.filemanager.delete_folder(path)
            
            return self.response.json({
                "message": 'Folder deleted...',
            })
        except Exception as e:
            print(e)
            
        return self.response.json({
            "message": "Folder doesn't exists!",
        })
    
    def delete_file(self):
        path = self.request.input('path')
        
        try:
            self.filemanager.delete_file(path)
            
            return self.response.json({
                "message": 'Folder deleted...',
            })
        except Exception as e:
            print(e)
            
        return self.response.json({
            "message": "Folder doesn't exists!",
        })
    
    