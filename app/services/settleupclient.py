import pyrebase

from app.models.transaction import Transaction
from app.utils.logging import setup_logger


class SettleUpClient:
    def __init__(self, firebase_config, settle_up_config, logger=None):
        firebase = pyrebase.initialize_app(firebase_config)
        auth = firebase.auth()
        auth.sign_in_with_email_and_password(settle_up_config["email"], settle_up_config["password"])
        self._current_user = auth.current_user["localId"]
        self._id_token = auth.current_user["idToken"]
        self._database = firebase.database()
        if logger:
            self._logger = logger
        else:
            self._logger = setup_logger("settle-up-client")

    def add_transaction(self, group_name: str, transaction: Transaction):
        self._logger.info(
            "add_transaction was called for group_name='{}', purpose='{}', time='{}' amount='{}' and who_paid_name='{}'".format(group_name,
                                                                                                                                transaction.purpose,
                                                                                                                                transaction.amount,
                                                                                                                                transaction.time,
                                                                                                                                transaction.whoPaidName))
        group_id = self._find_group_id(group_name)
        for_whom = self._create_for_whom_array(group_name)
        who_paid = self._create_who_paid(group_name, transaction.whoPaidName)
        if group_id and for_whom and who_paid:
            data = {"currencyCode": "EUR",
                    "dateTime": transaction.time,
                    "fixedExchangeRate": False,
                    "items": [
                        {
                            "amount": str(transaction.amount),
                            "forWhom": for_whom
                        }
                    ],
                    "purpose": transaction.purpose,
                    "type": "expense",
                    "whoPaid": who_paid}
            self._logger.info("try to send data='{}'".format(data))
            response = self._database.child("transactions").child(group_id).push(data, self._id_token)
            transaction_id = response["name"]
            return transaction_id
        else:
            self._logger.error("all of group_id='{}', for_whom='{}' and who_paid='{}' must be given".format(group_id, for_whom, who_paid))

    def _find_group_id(self, group_name: str):
        for group_id in self._get_user_group_ids():
            current_group = self._get_group(group_id).val()
            if current_group["name"] == group_name:
                return group_id
        self._logger.error("cannot identify group_id for group-name='{}'".format(group_name))
        return None

    def _get_user_group_ids(self):
        return self._database.child("userGroups").child(self._current_user).shallow().get(self._id_token).val()

    def _get_group(self, group_id: str):
        return self._database.child("groups").child(group_id).get(self._id_token)

    def _find_group_member_ids(self, group_name: str):
        group_id = self._find_group_id(group_name)
        if group_id:
            return self._database.child("members").child(group_id).shallow().get(self._id_token).val()
        return None

    def _create_for_whom_array(self, group_name: str):
        for_whom = []
        for member_id in self._find_group_member_ids(group_name):
            for_whom.append({"memberId": member_id, "weight": "1"})
        return for_whom

    def _find_group_members(self, group_name: str):
        group_id = self._find_group_id(group_name)
        if group_id:
            return self._database.child("members").child(group_id).get(self._id_token).val()
        return None

    def _find_member_id(self, group_name: str, who_paid_name: str):
        for member_id, group_member in self._find_group_members(group_name).items():
            if group_member["name"] == who_paid_name:
                return member_id
        self._logger.error("cannot identify member-id for who_paid_name='{}' in group='{}'".format(who_paid_name, group_name))
        return None

    def _create_who_paid(self, group_name: str, who_paid_name: str):
        who_paid_member_id = self._find_member_id(group_name, who_paid_name)
        return [{"memberId": who_paid_member_id, "weight": "1"}]

    def get_transaction(self, group_name: str, transaction_id: str):
        group_id = self._find_group_id(group_name)
        return self._database.child("transactions").child(group_id).child(transaction_id).get(self._id_token)

    def get_transactions(self, group_name: str):
        group_id = self._find_group_id(group_name)
        return self._database.child("transactions").child(group_id).get(self._id_token)

    def delete_transaction(self, group_name: str, transaction_id: str):
        group_id = self._find_group_id(group_name)
        self._database.child("transactions").child(group_id).child(transaction_id).remove(self._id_token)
