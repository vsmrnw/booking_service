from datetime import datetime

from fastapi import Depends, Request
from jose import JWTError, jwt

from app.config import settings
from app.exceptions import (
    IncorrectAuthDataException,
    IncorrectTokenFormatException,
    TokenExpiredException,
    TokenNotProvidedException,
)
from app.users.repository import UsersRepo


def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise TokenNotProvidedException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except JWTError:
        raise IncorrectTokenFormatException
    user_id: str = payload.get("sub")
    if not user_id:
        raise IncorrectAuthDataException
    user = await UsersRepo.find_one_or_none(id=int(user_id))
    if not user:
        raise IncorrectAuthDataException

    return user
