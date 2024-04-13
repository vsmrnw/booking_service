import pytest

from app.users.repository import UsersRepo


@pytest.mark.parametrize(
    "email,is_exists",
    [("test@test.com", True), ("test@example.com", True), (".....", False)],
)
async def test_find_user_by_id(email, is_exists):
    user = await UsersRepo.find_one_or_none(email=email)

    if is_exists:
        assert user
        assert user["email"] == email
    else:
        assert not user
