import logging
from collections import namedtuple

import pytest

from actions.card_actions import CardActions
from actions.funding_actions import FundingActions
from actions.payload_generator import PayloadGenerator
from actions.transaction_actions import TransactionActions
from actions.user_actions import UserActions
from base.base_test import BaseTest
from verifications.transaction_verifications import TransactionVerifications

logger = logging.getLogger(__name__)


class TestTransaction(BaseTest):

    @pytest.fixture(scope='module')
    def resources(self):
        # Create user
        user_client = UserActions()
        user_client.create_user(PayloadGenerator.user_payload())

        # Create card product
        card_client = CardActions()
        card_client.create_card_product(
            PayloadGenerator.card_product_payload())

        # Create card for the user using card product
        card_client.create_card(PayloadGenerator.card_payload(
            user_token=user_client.user_token,
            card_product_token=card_client.product_token))

        # Create Funding program source
        funding_client = FundingActions()
        funding_client.create_program_funding_source(
            PayloadGenerator.funding_source_payload())

        # Fund the user account
        funding_client.create_gpaorder(PayloadGenerator.gpaorder_payload(
            user_token=user_client.user_token, amount="100",
            funding_source_token=funding_client.funding_source_token))

        Data = namedtuple('Data',
                          'user_client, user_token, card_client,'
                          'card_product_token, card_token, funding_client, '
                          'funding_source_token, gpaorder_token')

        return Data(user_client=user_client,
                    user_token=user_client.user_token,
                    card_client=card_client,
                    card_product_token=card_client.product_token,
                    card_token=card_client.card_token,
                    funding_client=funding_client,
                    funding_source_token=funding_client.funding_source_token,
                    gpaorder_token=funding_client.gpaorder_token)

    @pytest.mark.all_test
    @pytest.mark.smoke_test
    # @pytest.mark.skip(reason="Test Disable")
    def test_create_transaction_success(self, resources):
        """
        Test create a new transaction  successfully
        """
        #
        # ================ CONFIGURATION ================
        #
        transaction_details = PayloadGenerator.transaction_payload(
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
        TransactionVerifications.verify_transaction_create_success(
            transaction, 15)

    @pytest.mark.all_test
    # @pytest.mark.skip(reason="Test Disable")
    def test_transaction_no_card_fund_decline(self, resources):
        """
        Test transaction decline when no card fund available
        """
        #
        # ================ CONFIGURATION ================
        #
        # Create user
        resources.user_client.create_user(PayloadGenerator.user_payload())

        # Create card product
        resources.card_client.create_card_product(PayloadGenerator.
                                                  card_product_payload())

        # Create card
        resources.card_client.create_card(PayloadGenerator.card_payload(
            user_token=resources.user_client.user_token,
            card_product_token=resources.card_client.product_token))

        #
        # ================ ACTION ================
        #
        transaction_details = PayloadGenerator.transaction_payload(
            amount="111", card_token=resources.card_client.card_token)

        transaction_actions = TransactionActions()
        transaction = transaction_actions.create_transaction(
            transaction_details)

        #
        # ================ VERIFICATION ================
        #
        TransactionVerifications.verify_transaction_decline(transaction)
