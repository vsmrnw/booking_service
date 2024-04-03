from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(HTTPException):
    status_code = status.HTTP_409_CONFLICT,
    detail = "User Already exists",


class IncorrectEmailOrPasswordException(HTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "Incorrect email or password",


class TokenExpiredException(HTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "Token expired",


class TokenNotProvidedException(HTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "Token didn't provided",


class IncorrectTokenFormatException(HTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "Incorrect token format"


class IncorrectAuthDataException(HTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "Incorrect auth data"
