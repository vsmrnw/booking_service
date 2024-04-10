import asyncio
from datetime import date, datetime, timedelta
from typing import List, Annotated, Optional

from fastapi import APIRouter, Query
from fastapi_cache.decorator import cache

from app.exceptions import CannotBookHotelForLongPeriod, \
    DateFromCannotBeAfterDateTo
from app.hotels.repository import HotelsRepo
from app.hotels.schemas import SHotelInfo, SHotel

router = APIRouter(
    prefix="/hotels",
    tags=["Hotels"]
)


@router.get("/{location}")
@cache(expire=30)
async def get_hotels_by_location_and_time(
        location: str,
        date_from: Annotated[
            date, Query(...,
                        description=f"e.g, {datetime.now().date()}")],
        date_to: Annotated[date, Query(...,
                                       description=f"e.g., {(datetime.now() + timedelta(days=14)).date()}")],
) -> List[SHotelInfo]:
    if date_from > date_to:
        raise DateFromCannotBeAfterDateTo
    if (date_to - date_from).days > 31:
        raise CannotBookHotelForLongPeriod
    hotels = await HotelsRepo.find_all(location, date_from, date_to)
    return hotels


@router.get("/id/{hotel_id}", include_in_schema=True)
async def get_hotel_by_id(
        hotel_id: int,
) -> Optional[SHotel]:
    return await HotelsRepo.find_one_or_none(id=hotel_id)
