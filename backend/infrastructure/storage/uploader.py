from django.conf import settings
from .cloudinary import CloudinaryStorage
from .local import LocalStorage


class StorageFactory:

    @staticmethod
    def get_storage():
        if settings.STORAGE_PROVIDER == "cloudinary":
            return CloudinaryStorage()

        return LocalStorage()