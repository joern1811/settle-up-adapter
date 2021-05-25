from pydantic import BaseModel


class Transaction(BaseModel):
    groupName: str
    purpose: str
    amount: float
    time: int
    whoPaidName: str
