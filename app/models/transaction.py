from pydantic import BaseModel


class Transaction(BaseModel):
    purpose: str
    amount: float
    time: int
    whoPaidName: str
