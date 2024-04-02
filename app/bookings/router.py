from fastapi import APIRouter
from app.bookings.repository import BookingRepo
from app.bookings.schemas import SBooking

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


@router.get("")
async def get_bookings() -> list[SBooking]:
    return await BookingRepo.find_all()
