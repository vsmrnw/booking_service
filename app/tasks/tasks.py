import smtplib

from pydantic import EmailStr

from app.config import settings
from app.tasks.celery import celery
from PIL import Image
from pathlib import Path

from app.tasks.email_templates import create_booking_confirmation_template


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


@celery.task
def send_booking_confirmation_email(
        booking: dict,
        email_to: EmailStr,
):
    email_to = settings.SMTP_USER
    msg_content = create_booking_confirmation_template(booking, email_to)

    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg_content)