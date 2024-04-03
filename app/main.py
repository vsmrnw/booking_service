from datetime import date
from typing import Annotated

from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel

from app.bookings.router import router as router_bookings
from app.users.router import router as router_users

app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)


class SHotel(BaseModel):
    address: str
    name: str
    stars: int


@app.get("/hotels")
async def get_hotels(
        location: str,
        date_from: date,
        date_to: date,
        has_spa: Annotated[bool, Query()] = None,
        stars: Annotated[int, Query(ge=1, le=5)] = None, ) -> list[SHotel]:
    return date_to, date_from
