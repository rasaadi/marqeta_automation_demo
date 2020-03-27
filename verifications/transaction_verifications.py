import logging

from base.base_test import BaseTest

logger = logging.getLogger(__name__)


class TransactionVerifications(BaseTest):
    @staticmethod
    def verify_transaction_create_success(transaction_response,
                                          transaction_amount):
        logger.info("verifying transaction creation successful")
        assert transaction_response is not None, "No transaction details found"
        assert transaction_response['transaction']['token'] is not None, \
            "No transaction token found"
        assert transaction_response['transaction'][
                   'amount'] == transaction_amount, \
            "Transaction amount mismatch"
