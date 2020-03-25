import json
import logging
from collections import namedtuple

import pytest

from actions.card_actions import CardActions
from actions.user_actions import UserActions
from base.base_test import BaseTest
from verifications.card_verifications import CardVerifications

logger = logging.getLogger(__name__)


class TestCardCreation(BaseTest):
    user_dict = {
        "first_name": "Joe",
        "last_name": "Sam",
        "active": True
    }
    user_details = json.dumps(user_dict)

    card_prod_dict = {
        "start_date": "2019-01-01",
        "name": "Example Card Product",
        "config": {
            "fulfillment": {
                "payment_instrument": "VIRTUAL_PAN"
            },
            "poi": {
                "ecommerce": True
            },
            "card_life_cycle": {
                "activate_upon_issue": True
            }
        }
    }
    card_prod_details = json.dumps(card_prod_dict)

    @pytest.fixture(scope='module')
    def resources(self):
        user_client = UserActions()
        user_client.create_user(self.user_details)

        card_client = CardActions()
        card_client.create_card_product(self.card_prod_details)

        Data = namedtuple('Data', 'user_token, card_product_token')

        return Data(user_token=user_client.user_token,
                    card_product_token=card_client.product_token)

    # @pytest.mark.skip(reason="no way of currently testing this")
    def test_create_card_success(self, resources):
        """
        Test create a new card  successfully
        """
        #
        # ================ CONFIGURATION ================
        #
        card_dict = {
            "user_token": resources.user_token,
            "card_product_token": resources.card_product_token
        }

        card_details = json.dumps(card_dict)

        #
        # ================ ACTION ================
        #
        card_client = CardActions()
        card = card_client.create_card(card_details)

        #
        # ================ VERIFICATION ================
        #
        card_verifications = CardVerifications()
        card_verifications.verify_card_creation_success(card, resources)

    # @pytest.mark.skip(reason="no way of currently testing this")
    def test_create_card_without_user_token_fail(self, resources):
        """
        Test create a new card  without user token unsuccessfully
        """
        #
        # ================ CONFIGURATION ================
        #
        card_dict = {
            "user_token": '',
            "card_product_token": resources.card_product_token
        }

        card_details = json.dumps(card_dict)

        #
        # ================ ACTION ================
        #
        card_client = CardActions()
        card = card_client.create_card(card_details)

        #
        # ================ VERIFICATION ================
        #
        card_verifications = CardVerifications()
        card_verifications.verify_card_creation_fail(card)