from datetime import date, datetime, timedelta
from fastapi import Query
from app.hotels.models import Hotels
from app.hotels.rooms.schemas import SRooms
from app.hotels.rooms.services import RoomServices
from app.hotels.router import router


@router.get('/{hotel_id}/rooms')
async def get_rooms(
    hotel_id: int,
    date_from: date = Query(..., description=f"Например, {datetime.now().date()}"),
    date_to: date = Query(..., description=f"Например, {(datetime.now() + timedelta(days=14)).date()}")) -> list[SRooms]:
    rooms = await RoomServices.find_all(hotel_id, date_from, date_to)
    return rooms