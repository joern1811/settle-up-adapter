from fastapi import APIRouter, Response

from app.models.transaction import Transaction
from app.core.config import SETTLE_UP_API_KEY, SETTLE_UP_AUTH_DOMAIN, SETTLE_UP_DATABASE_URL, SETTLE_UP_STORAGE_BUCKET, SETTLE_UP_USER, \
    SETTLE_UP_PASSWORD
from app.services.settleupclient import SettleUpClient

router = APIRouter()

firebase_config = {
    "apiKey": SETTLE_UP_API_KEY,
    "authDomain": SETTLE_UP_AUTH_DOMAIN,
    "databaseURL": SETTLE_UP_DATABASE_URL,
    "storageBucket": SETTLE_UP_STORAGE_BUCKET
}
settle_up_config = {
    "email": SETTLE_UP_USER,
    "password": SETTLE_UP_PASSWORD
}
settle_up_client = SettleUpClient(firebase_config, settle_up_config)


@router.post('/transactions')
def add_transaction(transaction: Transaction, response: Response):
    transaction_id = settle_up_client.add_transaction(transaction)
    response.headers['Location'] = "transactions/" + transaction_id
    return {"created": "true"}
