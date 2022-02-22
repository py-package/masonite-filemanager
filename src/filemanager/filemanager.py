from masonite.configuration import config
from .drivers.local_driver import LocalDriver
from .drivers.s3_driver import S3Driver


class FileManager:
    def __init__(self) -> None:
        self.conf = config("filemanager")

    def provider(self, driver=None):
        if driver is None:
            driver = self.conf.get("driver", "local")
        if driver == "local":
            return LocalDriver()
        if driver == "s3":
            return S3Driver()

        raise ModuleNotFoundError("Driver not found")
