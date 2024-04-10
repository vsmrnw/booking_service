import uuid
import shutil

from fastapi import APIRouter, UploadFile

from app.tasks.tasks import process_pic

router = APIRouter(
    prefix="/images",
    tags=["Upload images"]
)


@router.post("/hotels")
async def add_hotel_image(file: UploadFile):
    image_path = f"app/static/images/{uuid.uuid4()}.webp"
    with open(image_path, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    process_pic.delay(image_path)
    return {"info": f"file '{file.filename} saved'"}