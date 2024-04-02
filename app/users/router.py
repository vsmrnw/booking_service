from fastapi import APIRouter, HTTPException, status, Response

from app.users.auth import get_password_hash, authenticate_user, \
    create_access_token
from app.users.repository import UsersRepo
from app.users.schemas import SUserAuth

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Users"],
)


@router.post("/register")
async def register_user(user_data: SUserAuth):
    existing_user = await UsersRepo.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    hashed_password = get_password_hash(user_data.password)
    await UsersRepo.add(email=user_data.email, hashed_password=hashed_password)
    return {"message": "user created successfully"}


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    print(user)
    access_token = create_access_token({"sub": user})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return access_token
