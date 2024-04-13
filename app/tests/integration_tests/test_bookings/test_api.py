import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("room_id,date_from,date_to,status_code", [
    *[(4, "2026-05-01", "2026-05-15", 201)] * 8,
    (4, "2026-05-01", "2026-05-15", 409)
])
async def test_add_and_get_booking_endpoint(room_id, date_from, date_to,
                                            status_code,
                                            authenticated_ac: AsyncClient):
    response = await authenticated_ac.post("/bookings", params={
        "room_id": room_id,
        "date_from": date_from,
        "date_to": date_to,
    })
    assert response.status_code == status_code


async def test_get_and_delete_booking(authenticated_ac: AsyncClient):
    response = await authenticated_ac.get("/bookings")
    existing_bookings = [booking["id"] for booking in response.json()]
    for booking_id in existing_bookings:
        response = await authenticated_ac.delete(f"/bookings/{booking_id}")

    response = await authenticated_ac.get("/bookings")
    assert len(response.json()) == 0