import os
from django.conf import settings


class LocalStorage:
    def upload(self, file, folder="uploads"):
        path = os.path.join(settings.MEDIA_ROOT, folder, file.name)

        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, "wb+") as f:
            for chunk in file.chunks():
                f.write(chunk)

        return {
            "url": f"{settings.MEDIA_URL}{folder}/{file.name}",
            "public_id": path
        }

    def delete(self, public_id):
        if os.path.exists(public_id):
            os.remove(public_id)