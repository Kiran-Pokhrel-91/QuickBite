import cloudinary
import cloudinary.uploader
from django.conf import settings


# configure cloudinary once
cloudinary.config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_API_SECRET,
)


class CloudinaryStorage:
    def upload(self, file, folder="default"):
        result = cloudinary.uploader.upload(
            file,
            folder=folder
        )

        return {
            "url": result["secure_url"],
            "public_id": result["public_id"]
        }

    def delete(self, public_id):
        return cloudinary.uploader.destroy(public_id)