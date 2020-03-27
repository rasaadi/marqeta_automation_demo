import json
import logging
from collections import namedtuple

import pytest

from actions.card_actions import CardActions
from actions.payload_generator import PayloadGenerator
from actions.user_actions import UserActions
from base.base_test import BaseTest
from utils.utils_helper import UtilsHelper
from verifications.card_verifications import CardVerifications

logger = logging.getLogger(__name__)


class TestTransaction(BaseTest):
    timestamp = UtilsHelper()
    # user_dict = {
    #     "first_name": "Joe_" + timestamp.time_stamp(),
    #     "last_name": "Smith_" + timestamp.time_stamp(),
    #     "active": True
    # }
    # user_details = json.dumps(user_dict)
    #
    # card_prod_dict = {
    #     "start_date": timestamp.date(),
    #     "name": "Example Card Product",
    #     "config": {
    #         "fulfillment": {
    #             "payment_instrument": "VIRTUAL_PAN"
    #         },
    #         "poi": {
    #             "ecommerce": True
    #         },
    #         "card_life_cycle": {
    #             "activate_upon_issue": True
    #         }
    #     }
    # }
    # card_prod_details = json.dumps(card_prod_dict)
    #
    # card_dict = {
    #     "user_token": "**USER TOKEN**",
    #     "card_product_token": "**CARD PRODUCT TOKEN**"
    # }

    @pytest.fixture(scope='module')
    def resources(self):
        # Create user
        user_client = UserActions()
        user_client.create_user(PayloadGenerator.get_user_payload())
        # user_client.create_user(self.user_details)

        # Create card product
        card_client = CardActions()
        card_client.create_card_product(PayloadGenerator.get_card_product_payload())
        # card_client.create_card_product(self.card_prod_details)

        # Create card for the user using card product
        # self.card_dict.update(user_token=user_client.user_token,
        #                       card_product_token=card_client.product_token)
        # card_details = json.dumps(self.card_dict)


        # card_client.create_card(card_details)

        card_client.create_card(PayloadGenerator.get_card_payload(user_token=user_client.user_token,
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
        logger.info("card token: {}".format(resources.card_token))


        #
        # ================ ACTION ================
        #


        #
        # ================ VERIFICATION ================
        #

