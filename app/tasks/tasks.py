from app.tasks.celery import celery
from PIL import Image
from pathlib import Path


@celery.task
def process_pic(
        path: str,
):
    image_path = Path(path)
    image = Image.open(image_path)
    image_resized_bigger = image.resize((1000, 500))
    image_resized_smaller = image.resize((200, 100))
    image_resized_bigger.save(
        f"app/static/images/resized_1000_500_{image_path.name}")
    image_resized_smaller.save(
        f"app/static/images/resized_200_100_{image_path.name}")
