import asyncio
from datetime import date, datetime, timedelta
from typing import List, Optional
from fastapi import APIRouter, Query
from fastapi_cache.decorator import cache
from app.exceptions import (
    CannotBookHotelForLongPeriod, DateFromCannotBeAfterDateTo
)
from app.hotels.schemas import SHotels, SHotelsInfo
from app.hotels.services import HotelServices

router = APIRouter(prefix='/hotels', tags=['Отели'])


@router.get('')
@cache(expire=20)
async def get_hotels_by_location_and_time(
    location: str,
    date_from: date = Query(..., description=f"Например, {datetime.now().date()}"),
    date_to: date = Query(..., description=f"Например, {(datetime.now() + timedelta(days=14)).date()}")) -> List[SHotelsInfo]:
    if date_from > date_to:
        raise DateFromCannotBeAfterDateTo
    if (date_to - date_from).days > 31:
        raise CannotBookHotelForLongPeriod
    await asyncio.sleep(3)
    hotels = await HotelServices.find_all(location, date_from, date_to)
    return hotels


@router.get('/id/{hotel_id}', include_in_schema=True)
# Этот эндпоинт используется для фронтенда, когда мы хотим отобразить все
# номера в отеле и информацию о самом отеле. Этот эндпоинт как раз отвечает за информацию
# об отеле.
# В нем нарушается правило именования эндпоинтов: конечно же, /id/ здесь избыточен.
# Тем не менее, он используется, так как эндпоинтом ранее мы уже задали получение
# отелей по их локации вместо id.
async def get_hotel_by_id(
    hotel_id: int,
) -> Optional[SHotels]:
    return await HotelServices.find_one_or_none(id=hotel_id)
