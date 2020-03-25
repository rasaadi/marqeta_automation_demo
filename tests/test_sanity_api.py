import json
import logging

import pytest

from actions.card_actions import CardActions
from actions.user_actions import UserActions
from base.base_test import BaseTest

logger = logging.getLogger(__name__)


class TestSanityApi(BaseTest):
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_create_user_successfully(self):
        """
        Test create new user successfully
        """
        #
        # ================ CONFIGURATION ================
        #
        user_dict = {
            "first_name": "Joe",
            "last_name": "Sam",
            "active": True
        }
        user_details = json.dumps(user_dict)

        #
        # ================ ACTION ================
        #
        user_client = UserActions()
        user = user_client.create_user(user_details)

        #
        # ================ VERIFICATION ================
        #
        logger.info(user.text)

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_create_card_product_successfully(self):
        """
        Test create new card successfully
        """
        #
        # ================ CONFIGURATION ================
        #
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

        #
        # ================ ACTION ================
        #
        card_client = CardActions()
        card_product = card_client.create_card_product(card_prod_details)

        #
        # ================ VERIFICATION ================
        #
        logger.info(card_product.text)

    def test_create_program_funding_source_successfully(self):
        """
        Test create new program funding source successfully
        """
        #
        # ================ CONFIGURATION ================
        #
        fund_source_dict = {
                            "name": "Program Funding"
                        }

        fund_source_details = json.dumps(fund_source_dict)

        #
        # ================ ACTION ================
        #
        card_client = CardActions()
        funding_source = card_client.create_program_funding_source(
            fund_source_details)

        #
        # ================ VERIFICATION ================
        #
        logger.info(funding_source)


    @pytest.mark.skip(reason="no way of currently testing this")
    def test_create_card_successfully(self):
        """
        Test create new card product successfully
        """
        #
        # ================ CONFIGURATION ================
        #
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

        #
        # ================ ACTION ================
        #
        card_client = CardActions()
        card_product = card_client.create_card_product(card_prod_details)

        #
        # ================ VERIFICATION ================
        #
        logger.info(card_product.text)