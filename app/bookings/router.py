from datetime import date

from fastapi import APIRouter, Depends, status
from pydantic import parse_obj_as

from app.bookings.repository import BookingRepo
from app.bookings.schemas import SBooking, SNewBooking
from app.exceptions import RoomCannotBeBooked
from app.tasks.tasks import send_booking_confirmation_email
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[
    SBooking]:
    return await BookingRepo.find_all(user_id=user)


@router.post("", status_code=status.HTTP_201_CREATED)
async def add_booking(
        room_id: int, date_from: date, date_to: date,
        user: Users = Depends(get_current_user),
):
    booking = await BookingRepo.add(
        user.id,
        room_id,
        date_from,
        date_to)
    if not booking:
        raise RoomCannotBeBooked
    booking = parse_obj_as(SNewBooking, booking).dict()
    send_booking_confirmation_email.delay(booking, user.email)
    return booking


@router.delete("/{booking_id}")
async def remove_booking(
        booking_id: int,
        user: Users = Depends(get_current_user)
):
    await BookingRepo.delete(id=booking_id, user_id=user)
