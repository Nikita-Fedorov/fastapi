from pydantic import BaseModel


class SRooms(BaseModel):
    id: int
    hotel_id: int
    name: str
    description: str
    services: list
    price: int
    quantity: int
    image_id: int

    class Config:
        from_attributes = True


class SRoomsInfo(SRooms):
    total_cost: int
    rooms_left: int

    class Config:
        from_attributes = True
