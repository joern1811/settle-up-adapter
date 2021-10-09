from fastapi import APIRouter, Response

from app.core.config import SETTLE_UP_FIREBASE_API_KEY, SETTLE_UP_USER, \
    SETTLE_UP_PASSWORD, SETTLE_UP_FIREBASE_PROJECT_NAME
from app.models.transaction import Transaction
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


# for test reasons, not mapped to transaction model
@router.get('/groups/{group_name}/transactions/', tags=["transactions"])
def get_transactions(group_name: str):
    transactions = settle_up_client.get_transactions(group_name)
    return transactions


@router.post('/groups/{group_name}/transactions', tags=["transactions"])
def add_transaction(group_name: str, transaction: Transaction, response: Response):
    transaction_id = settle_up_client.add_transaction(group_name, transaction)
    response.headers['Location'] = "transactions/" + transaction_id
    return {"created": "true"}


@router.delete('/groups/{group_name}/transactions', tags=["transactions"])
def delete_group_transactions(group_name: str):
    settle_up_client.delete_group_transactions(group_name)


@router.delete('/groups/{group_name}/transactions/{transaction_id}', tags=["transactions"])
def delete_transaction(group_name: str, transaction_id: str):
    settle_up_client.delete_transaction(group_name, transaction_id)
