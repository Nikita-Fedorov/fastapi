from datetime import date
from fastapi import APIRouter, Depends
from pydantic import parse_obj_as
from app.bookings.schemas import SBooking, SBookingRoom
from app.bookings.services import BookingService
from app.exceptions import RoomCannotBeBooked
from app.tasks.tasks import send_booking_confirmation_email
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирования']
)


@router.get('')
async def get_booking(
    user: Users = Depends(get_current_user)
) -> list[SBookingRoom]:
    return await BookingService.get_booked_rooms(user.id)


@router.post('')
async def add_booking(
    room_id: int,
    date_from: date,
    date_to: date,
    user: Users = Depends(get_current_user)
):
    booking = await BookingService.add(user.id, room_id, date_from, date_to)
    booking_dict = parse_obj_as(SBooking, booking).dict()
    send_booking_confirmation_email.delay(booking_dict, user.email)
    if not booking:
        raise RoomCannotBeBooked
    return booking_dict


@router.delete('/{booking_id}')
async def del_bookings(
    booking_id: int,
    user: Users = Depends(get_current_user)
):
    await BookingService.delete(id=booking_id, user_id=user.id)
