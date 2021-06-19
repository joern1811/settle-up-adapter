from fastapi import APIRouter, Response

from app.models.transaction import Transaction
from app.core.config import SETTLE_UP_FIREBASE_API_KEY, SETTLE_UP_USER, \
    SETTLE_UP_PASSWORD, SETTLE_UP_FIREBASE_PROJECT_NAME
from app.services.settleupclient import SettleUpClient

router = APIRouter()

firebase_config = {
    "apiKey": SETTLE_UP_FIREBASE_API_KEY,
    "authDomain": "{}.firebaseapp.com".format(SETTLE_UP_FIREBASE_PROJECT_NAME),
    "databaseURL": "https://{}.firebaseio.com".format(SETTLE_UP_FIREBASE_PROJECT_NAME),
    "storageBucket": "{}.appspot.com".format(SETTLE_UP_FIREBASE_PROJECT_NAME),
}
settle_up_config = {
    "email": SETTLE_UP_USER,
    "password": SETTLE_UP_PASSWORD
}
settle_up_client = SettleUpClient(firebase_config, settle_up_config)


@router.post('/groups/{group_name}/transactions', tags=["transactions"])
def add_transaction(group_name: str, transaction: Transaction, response: Response):
    transaction_id = settle_up_client.add_transaction(group_name, transaction)
    response.headers['Location'] = "transactions/" + transaction_id
    return {"created": "true"}
