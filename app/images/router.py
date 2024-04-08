import uuid
import shutil

from fastapi import APIRouter, UploadFile

router = APIRouter(
    prefix="/images",
    tags=["Upload images"]
)


@router.post("/hotels")
async def add_hotel_image(file: UploadFile):
    with open(f"app/static/images/{uuid.uuid4()}.webp", "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    return {"info": f"file '{file.filename} saved'"}