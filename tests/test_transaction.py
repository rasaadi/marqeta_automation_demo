import json
import logging
from collections import namedtuple

import pytest

from actions.card_actions import CardActions
from actions.payload_generator import PayloadGenerator
from actions.transaction_actions import TransactionActions
from actions.user_actions import UserActions
from base.base_test import BaseTest
from utils.utils_helper import UtilsHelper
from verifications.card_verifications import CardVerifications

logger = logging.getLogger(__name__)


class TestTransaction(BaseTest):

    @pytest.fixture(scope='module')
    def resources(self):
        # Create user
        user_client = UserActions()
        user_client.create_user(PayloadGenerator.get_user_payload())

        # Create card product
        card_client = CardActions()
        card_client.create_card_product(
            PayloadGenerator.get_card_product_payload())

        # Create card for the user using card product
        card_client.create_card(PayloadGenerator.get_card_payload(
            user_token=user_client.user_token,
            card_product_token=card_client.product_token))

        Data = namedtuple('Data',
                          'user_client, user_token, card_client,'
                          'card_product_token, card_token')

        return Data(user_client=user_client,
                    user_token=user_client.user_token,
                    card_client=card_client,
                    card_product_token=card_client.product_token,
                    card_token=card_client.card_token)

    # @pytest.mark.skip(reason="Test Disable")
    def test_create_transaction_success(self, resources):
        """
        Test create a new transaction  successfully
        """
        #
        # ================ CONFIGURATION ================
        #
        transaction_details = PayloadGenerator.get_transaction_payload(
            amount="15", card_token=resources.card_token)

        #
        # ================ ACTION ================
        #
        transaction_actions = TransactionActions()
        transaction = transaction_actions.create_transaction(
            transaction_details)

        #
        # ================ VERIFICATION ================
        #
        logger.info(transaction)
