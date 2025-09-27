from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    quantity: int
    price: float

class UpdateItem(BaseModel):
    quantity: Optional[int] = None
    price: Optional[float] = None
