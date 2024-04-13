import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "email,password,status_code",
    [
        ("new@user.com", "test", 201),
        ("new@user.com", "test1", 409),
        ("testsssss", "test0", 422),
    ],
)
async def test_register_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post(
        "/auth/register",
        json={
            "email": email,
            "password": password,
        },
    )
    assert response.status_code == status_code


@pytest.mark.parametrize(
    "email,password,status_code",
    [
        ("test@test.com", "test", 200),
        ("test@example.com", "test", 200),
        ("wrongesadmail@example.com", "test", 401),
    ],
)
async def test_login_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post(
        "/auth/login",
        json={
            "email": email,
            "password": password,
        },
    )

    assert response.status_code == status_code
