from app.bookings.models import Bookings
from app.repository.base import BaseDAO


class BookingDAO(BaseDAO):
    model = Bookings
