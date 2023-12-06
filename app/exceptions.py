from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'Пользователь уже существует'


class IncorrectEmailOrPasswordException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Неверный email или пароль'


class TokenExpiredException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Токен истек'


class TokenAbcentException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Токен отсутсвует'


class IncorrectTokenFormatExceptions(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Неверный формат токена'


class UserIsNotPresent(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED


class RoomCannotBeBooked(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'Не осатлось свободных номеров'


class DateFromCannotBeAfterDateTo(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'Дата заезда не может быть раньше даты выезда'


class CannotBookHotelForLongPeriod(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'Слишком большой период'
