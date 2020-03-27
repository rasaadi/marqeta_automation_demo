import json
import logging
import random

from utils.utils_helper import UtilsHelper

logger = logging.getLogger(__name__)


class PayloadGenerator:
    timestamp = UtilsHelper()

    @staticmethod
    def user_payload():
        logger.info("Generating user payload")
        user_dict = {
            "first_name": "Joe_" + PayloadGenerator.timestamp.time_stamp(),
            "last_name": "Smith_" + PayloadGenerator.timestamp.time_stamp(),
            "active": True
        }
        user_payload = json.dumps(user_dict)
        return user_payload

    @staticmethod
    def card_product_payload():
        logger.info("Generating card product payload")
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
    def card_payload(**kwargs):
        logger.info("Generating card payload")
        card_dict = {
            "user_token": "**USER TOKEN**",
            "card_product_token": "**CARD PRODUCT TOKEN**"
        }

        if len(kwargs) >= 2:
            for key in kwargs:
                for k in card_dict:
                    if key == k:
                        card_dict[k] = kwargs[key]
        else:
            logger.error("Insufficient card details provided")

        card_payload = json.dumps(card_dict)
        return card_payload

    @staticmethod
    def funding_source_payload():
        logger.info("Generating program funding source payload")
        funding_dict = {
            "name": "Program_Funding_" +
                    PayloadGenerator.timestamp.time_stamp()
        }

        funding_payload = json.dumps(funding_dict)
        return funding_payload

    @staticmethod
    def gpaorder_payload(**kwargs):
        logger.info("Generating gpaorder payload")
        gpaorder_dict = {
            "user_token": "**USER TOKEN**",
            "amount": "1000",
            "currency_code": "USD",
            "funding_source_token": "**PROGRAM FUNDING SOURCE TOKEN**"
        }

        if len(kwargs) >= 2:
            for key in kwargs:
                for k in gpaorder_dict:
                    if key == k:
                        gpaorder_dict[k] = kwargs[key]
        else:
            logger.error("Insufficient gpaorder details provided")

        gpaorder_payload = json.dumps(gpaorder_dict)
        return gpaorder_payload

    @staticmethod
    def user_account_funding_payload(**kwargs):
        logger.info("Generating user account funding payload")
        account_dict = {
            "user_token": "**USER TOKEN**",
            "amount": "1000",
            "currency_code": "USD",
            "funding_source_token": "**PROGRAM FUNDING SOURCE TOKEN**"
        }

        if len(kwargs) >= 2:
            for key in kwargs:
                for k in account_dict:
                    if key == k:
                        account_dict[k] = kwargs[key]
        else:
            logger.error("Insufficient account funding details provided")

        account_fund_payload = json.dumps(account_dict)
        return account_fund_payload

    @staticmethod
    def transaction_payload(**kwargs):
        logger.info("Generating transaction payload")
        transaction_dict = {
            "amount": "10",
            "mid": str(random.randrange(1000000000, 9999999999)),
            "card_token": "**CARD TOKEN FROM PREVIOUS STEP**"
        }

        if len(kwargs) >= 1:
            for key in kwargs:
                for k in transaction_dict:
                    if key == k:
                        transaction_dict[k] = kwargs[key]
        else:
            logger.error("Insufficient transaction details provided")

        transaction_payload = json.dumps(transaction_dict)
        return transaction_payload
