from datetime import datetime

from fastapi import Request, Depends
from jose import jwt, JWTError

from app.config import settings
from app.exceptions import TokenExpiredException, TokenNotProvidedException, \
    IncorrectTokenFormatException, IncorrectAuthDataException
from app.users.repository import UsersRepo


def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise TokenNotProvidedException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY,
                             settings.ALGORITHM)
    except JWTError:
        raise IncorrectTokenFormatException
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpiredException
    user_id: str = payload.get("sub")
    if not user_id:
        raise IncorrectAuthDataException
    user = await UsersRepo.find_by_id(int(user_id))
    if not user:
        raise IncorrectAuthDataException

    return user
