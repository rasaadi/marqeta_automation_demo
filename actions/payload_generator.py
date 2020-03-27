import json
import logging

from utils.utils_helper import UtilsHelper

logger = logging.getLogger(__name__)


class PayloadGenerator:
    timestamp = UtilsHelper()

    @staticmethod
    def get_user_payload():
        logger.info("Generation user payload")
        user_dict = {
            "first_name": "Joe_" + PayloadGenerator.timestamp.time_stamp(),
            "last_name": "Smith_" + PayloadGenerator.timestamp.time_stamp(),
            "active": True
        }
        user_payload = json.dumps(user_dict)
        return user_payload


    @staticmethod
    def get_card_product_payload():
        logger.info("Generation card product payload")
        card_prod_dict = {
            "start_date": PayloadGenerator.timestamp.date(),
            "name": "New_Card_Product_" + PayloadGenerator.timestamp.date(),
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
        card_prod_payload = json.dumps(card_prod_dict)
        return card_prod_payload

    @staticmethod
    def get_card_payload(**kwargs):
        logger.info("Generation card payload")
        card_dict = {
            "user_token": "**USER TOKEN**",
            "card_product_token": "**CARD PRODUCT TOKEN**"
        }
        if len(kwargs) >= 2:
            for key in kwargs:
                for k, v in card_dict.items():
                    if key == k:
                        card_dict[k] = kwargs[key]
        else:
            logger.error("Insufficient card details provided")

        card_payload = json.dumps(card_dict)
        return card_payload

