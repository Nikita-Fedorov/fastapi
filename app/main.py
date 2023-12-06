from fastapi import FastAPI

from app.bookings.router import router as router_bookings
from app.users.router import router as router_users
from app.hotels.router import router as router_hotels
from app.hotels.rooms.router import router as router_rooms
from app.pages.router import router as router_pages


app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_hotels)
app.include_router(router_rooms)
app.include_router(router_pages)


# class SHotel(BaseModel):
#     adress: str
#     name: str
#     stars: int


# @app.get('/hotels')
# def get_hotels(
#     location: str,
#     date_from: date,
#     date_to: date,
#     has_spa: Optional[bool] = None,
#     stars: Optional[int] = Query(None, ge=1, le=5),
# ) -> list[SHotel]:
#     hotels = [
#         {
#             'adress': 'Москва, Охотный ряд, 2',
#             'name': 'Four Seasons',
#             'stars': 5,
#         },
#     ]
#     return hotels


# class SBooking(BaseModel):
#     room_id: int
#     date_from: date
#     date_to: date


# @app.post('/bookings')
# def add_booking(booking: SBooking):
#     pass
