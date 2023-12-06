from datetime import datetime
from fastapi import Depends, Request
from jose import jwt, JWTError

from app.config import settings
from app.exceptions import (
    IncorrectTokenFormatExceptions, TokenAbcentException,
    TokenExpiredException, UserIsNotPresent
)
from app.users.services import UsersServices


def get_token(request: Request):
    token = request.cookies.get('booking_access_token')
    if not token:
        raise TokenAbcentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITMS
        )
    except JWTError:
        raise IncorrectTokenFormatExceptions
    expire: str = payload.get('exp')
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpiredException
    user_id: str = payload.get('sub')
    if not user_id:
        raise UserIsNotPresent
    user = await UsersServices.find_by_id(int(user_id))
    if not user:
        raise UserIsNotPresent
    return user
