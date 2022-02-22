"""A FileManagerProvider Service Provider."""

import os
import pathlib
from masonite.packages import PackageProvider
from jinja2 import Environment, FileSystemLoader

# from jinja2 import FileSystemLoader
# #..
# .add_location(os.path.join(current_path, '../views'), loader=FileSystemLoader)

class FileManagerProvider(PackageProvider):

    def configure(self):
        """Register objects into the Service Container."""
        (
            self.root("filemanager")
            .name("filemanager")
            .config("config/filemanager.py", publish=True)
            # .views("templates", publish=False)
            .routes("routes/route.py")
        )

    def register(self):
        super().register()
        from wsgi import application

        current_path = pathlib.Path(__file__).parent.parent.resolve()
        application.make('view').add_location(os.path.join(current_path, 'templates'), loader=FileSystemLoader)

    def boot(self):
        """Boots services required by the container."""
        pass
