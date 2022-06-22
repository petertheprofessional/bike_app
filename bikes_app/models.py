from pydantic import BaseModel


class Bike(BaseModel):
    id: str
    name: str
    manufacturer: str
    year: str


class Person(BaseModel):
    name: str
    email: str


class Client(Person):
    id: int
    address: str


class Partner(Person):
    bike: Bike


class Bill:
    status: str = "Pending"
    client: str
    partner: str
    bill_strategy: str
    total_price: int = 0