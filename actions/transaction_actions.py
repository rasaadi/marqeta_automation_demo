import logging

from actions.api_generic_actions import ApiGenericActions

logger = logging.getLogger(__name__)


class TransactionActions(ApiGenericActions):
    def __init__(self):
        super().__init__()
        self.transaction_token = None
        self.url = self.base_url + "simulate/authorization"

    def create_transaction(self, transaction_payload):
        logger.info("Creating a new transaction")

        if transaction_payload is not None:
            response_msg, http_code = self.post(self.url, transaction_payload)

            try:
                transaction = response_msg.json()
            except ValueError as ve:
                logger.error("Failed to convert transaction details into JSON")

            if http_code == 201:
                self.transaction_token = transaction['transaction']['token']
            elif http_code == 409:
                logger.error(
                    "Request already processed with a different payload")
            # elif http_code == 422:
            #     logger.error("Rule violations or declined transactions from "
            #                  "funding source")
            else:
                logger.error("User input error/Bad request")
        else:
            logger.error("Missing transaction details")

        return transaction
