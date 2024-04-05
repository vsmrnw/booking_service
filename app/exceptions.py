from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "User Already exists"


class IncorrectEmailOrPasswordException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect email or password"


class TokenExpiredException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token expired"


class TokenNotProvidedException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token didn't provided"


class IncorrectTokenFormatException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect token format"


class IncorrectAuthDataException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect auth data"
