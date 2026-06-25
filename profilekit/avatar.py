from pathlib import Path
from PIL import Image
import shutil
import uuid

AVATAR_FOLDER = Path("avatars")
AVATAR_FOLDER.mkdir(exist_ok=True)


def save_avatar(image_path):
    image_path = Path(image_path)

    if not image_path.exists():
        return ""

    new_name = f"{uuid.uuid4().hex}{image_path.suffix}"
    destination = AVATAR_FOLDER / new_name

    image = Image.open(image_path)
    image = image.resize((160, 160))
    image.save(destination)

    return str(destination)
