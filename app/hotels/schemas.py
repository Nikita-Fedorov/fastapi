from pydantic import BaseModel


class SHotels(BaseModel):
    id: int
    name: str
    location: str
    services: list
    rooms_quantity: int

    class Config:
        from_attributes = True


class SHotelsInfo(SHotels):
    rooms_left: int

    class Config:
        from_attributes = True
