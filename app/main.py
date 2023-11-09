from fastapi import FastAPI, Query
from datetime import date
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class SHotel(BaseModel):
    adress: str
    name: str
    stars: int


@app.get('/hotels')
def get_hotels(
    location: str,
    date_from: date,
    date_to: date,
    has_spa: Optional[bool] = None,
    stars: Optional[int] = Query(None, ge=1, le=5),
) -> list[SHotel]:
    hotels = [
        {
            'adress': 'Москва, Охотный ряд, 2',
            'name': 'Four Seasons',
            'stars': 5,
        },
    ]
    return hotels


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post('/bookings')
def add_booking(booking: SBooking):
    pass
