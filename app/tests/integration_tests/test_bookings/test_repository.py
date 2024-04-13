from app.bookings.repository import BookingRepo
from datetime import datetime


async def test_add_and_get_booking():
    new_booking = await BookingRepo.add(
        user_id=2,
        room_id=2,
        date_from=datetime.strptime("2023-07-10", "%Y-%m-%d"),
        date_to=datetime.strptime("2023-07-24", "%Y-%m-%d")
    )
    assert new_booking.user_id == 2
    assert new_booking.room_id == 2

    new_booking = await BookingRepo.find_one_or_none(id=new_booking.id)

    assert new_booking  is not None