from pydantic import BaseModel

class Address(BaseModel):
    name: str
    city: str
    state: str
    pincode: str
    latitude: str
    longitude: str