from app.bookings.models import Bookings
from app.repository.base import BaseRepo


class BookingRepo(BaseRepo):
    model = Bookings
