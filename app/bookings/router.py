from fastapi import APIRouter
from app.bookings.repository import BookingRepo

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


@router.get("")
async def get_bookings():
    return await BookingRepo.find_all()
