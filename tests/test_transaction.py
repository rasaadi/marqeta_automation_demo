import json
import logging
from collections import namedtuple

import pytest

from actions.card_actions import CardActions
from actions.user_actions import UserActions
from base.base_test import BaseTest
from utils.utils_helper import UtilsHelper
from verifications.card_verifications import CardVerifications

logger = logging.getLogger(__name__)


class TestTransaction(BaseTest):
    timestamp = UtilsHelper()
    user_dict = {
        "first_name": "Joe_" + timestamp.time_stamp(),
        "last_name": "Smith_" + timestamp.time_stamp(),
        "active": True
    }
    user_details = json.dumps(user_dict)

    card_prod_dict = {
        "start_date": timestamp.date(),
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

    card_dict = {
        "user_token": "**USER TOKEN**",
        "card_product_token": "**CARD PRODUCT TOKEN**"
    }

    card_details = json.dumps(card_dict)

    @pytest.fixture(scope='module')
    def resources(self):
        user_client = UserActions()
        user_client.create_user(self.user_details)

        card_client = CardActions()
        card_client.create_card_product(self.card_prod_details)

        Data = namedtuple('Data',
                          'user_client, user_token, card_client,'
                          'card_product_token')

        return Data(user_client=user_client,
                    user_token=user_client.user_token,
                    card_client=card_client,
                    card_product_token=card_client.product_token)

    # @pytest.mark.skip(reason="Test Disable")
    def test_create_transaction_success(self, resources):
        """
        Test create a new transaction  successfully
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
        card = resources.card_client.create_card(card_details)

        #
        # ================ VERIFICATION ================
        #
        resources.card_verification.verify_card_creation_success(card,
                                                                 resources)
