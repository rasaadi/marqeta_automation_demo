import logging

from actions.api_generic_actions import ApiGenericActions

logger = logging.getLogger(__name__)


class TransactionActions(ApiGenericActions):
    def __init__(self):
        super().__init__()
        self.transaction_token = None
        self.url = self.base_url + "simulate/authorization"

    def create_transaction(self, transaction_payload):
        """
        method to create  transaction
        :param transaction_payload: request payload containing transaction
        details
        :return: transaction(json)
        """
        logger.info("Creating a new transaction")

        if transaction_payload is not None:
            response_msg, http_code = self.post(self.url, transaction_payload)

            try:
                transaction = response_msg.json()
            except ValueError as ve:
                logger.error("Failed to convert transaction details into JSON")

            if http_code == 201:
                self.transaction_token = transaction['transaction']['token']
            else:
                logger.error("Error in the request, HTTP code: {}"
                             .format(http_code))
        else:
            logger.error("Missing transaction details")

        return transaction
