from fastapi import APIRouter, Depends
from app.bookings.repository import BookingRepo
from app.bookings.schemas import SBooking
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[
    SBooking]:
    return await BookingRepo.find_all(user_id=user.id)
