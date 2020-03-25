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


class TestCardCreation(BaseTest):
    timestamp = UtilsHelper()
    card_verifications = CardVerifications()
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

    # @pytest.mark.skip(reason="Test Disable")
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
        # card_verifications = CardVerifications()
        self.card_verifications.verify_card_creation_success(card, resources)

    # @pytest.mark.skip(reason="Test Disable")
    def test_create_multiple_cards_same_user_product_success(self, resources):
        """
        Test create multiple cards for same user and card product successfully
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
        card1 = card_client.create_card(card_details)
        card2 = card_client.create_card(card_details)

        #
        # ================ VERIFICATION ================
        #
        # card_verifications = CardVerifications()
        self.card_verifications\
            .verify_multiple_cards_same_user_product_success(card1, card2)

    # @pytest.mark.skip(reason="Test Disable")
    def test_create_personalized_card_with_name_success(self, resources):
        """
        Test create a new personalized card with custom name successfully
        """
        #
        # ================ CONFIGURATION ================
        #
        custom_name = "custom_name_" + self.timestamp.time_stamp()
        card_dict = {
            "user_token": resources.user_token,
            "card_product_token": resources.card_product_token,
            "fulfillment": {
                "card_personalization": {
                    "text": {
                        "name_line_1": {
                            "value": custom_name
                        }
                    }
                }
            }
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
        # card_verifications = CardVerifications()
        self.card_verifications.verify_card_creation_custom_name_success(card,
                                                                    custom_name)

    # @pytest.mark.skip(reason="Test Disable")
    def test_create_card_without_user_token_fail(self, resources):
        """
        Test create a new card without user token unsuccessfully
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
        # card_verifications = CardVerifications()
        self.card_verifications.verify_no_user_token_card_creation_fail(card)

    # @pytest.mark.skip(reason="Test Disable")
    def test_create_card_with_invalid_product_token_fail(self, resources):
        """
        Test create a new card  with invalid product token unsuccessfully
        """
        #
        # ================ CONFIGURATION ================
        #
        card_dict = {
            "user_token": resources.user_token,
            "card_product_token": 'invalid_token'
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
        # card_verifications = CardVerifications()
        self.card_verifications\
            .verify_invalid_product_token_card_creation_fail(
            card)
