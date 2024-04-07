from datetime import date, datetime, timedelta
from typing import List

from fastapi import APIRouter, Query

from app.exceptions import CannotBookHotelForLongPeriod, \
    DateFromCannotBeAfterDateTo
from app.hotels.repository import HotelsRepo
from app.hotels.schemas import SHotelInfo

router = APIRouter(
    prefix="/hotels",
    tags=["Hotels"]
)


@router.get("/{location}")
async def get_hotels_by_location_and_time(
        location: str,
        date_from: date = Query(...,
                                description=f"e.g., {datetime.now().date()}"),
        date_to: date = Query(...,
                              description=f"e.g, {(datetime.now() + timedelta(days=14)).date()}"),
) -> List[SHotelInfo]:
    if date_from > date_to:
        raise DateFromCannotBeAfterDateTo
    if (date_to - date_from).days > 31:
        raise CannotBookHotelForLongPeriod
    hotels = await HotelsRepo.find_all(location, date_from, date_to)
    return hotels


@router.get("/{location}")
async def get_hotels(location: str):
    return await HotelsRepo.find_all(location=location)
