import logging

from base.base_test import BaseTest

logger = logging.getLogger(__name__)


class CardVerifications(BaseTest):
    def verify_card_creation_success(self, card_api_response,
                                     card_resources):
        logger.info("verifying card creation successful")
        assert card_api_response is not None, "No card object details found"
        assert card_api_response['token'] is not None, "No card token found"
        assert card_api_response['user_token'] == card_resources.user_token, \
            "User token mismatch"
        assert card_api_response['card_product_token'] == card_resources. \
            card_product_token, "Card product token mismatch"

    def verify_no_user_token_card_creation_fail(self, card_api_response):
        logger.info("verifying card creation without user token failed")
        assert card_api_response is not None, "No card object details found"
        assert card_api_response['error_code'] == '400001', \
            "Mismatch error code"
        assert card_api_response['error_message'] is not None, \
            "No error msg found"

    def verify_invalid_product_token_card_creation_fail(self,
                                                        card_api_response):
        logger.info("verifying card creation with invalid product token "
                    "failed")
        assert card_api_response is not None, "No card object details found"
        assert card_api_response['error_code'] == '400016', \
            "Mismatch error code"
        assert card_api_response['error_message'] == 'Card product not ' \
                                                     'found', \
            "Mismatch error msg"

    def verify_card_creation_custom_name_success(self, card_api_response,
                                                 personalized_name):
        logger.info("verifying card creation with custom name successful")
        assert card_api_response is not None, "No card object details found"
        assert card_api_response['token'] is not None, "No card token found"
        # Need better way to parse nested json msg
        assert \
        card_api_response['fulfillment']['card_personalization']['text'][
            'name_line_1']['value'] == personalized_name, "Custom name " \
                                                          "mismatch"

    def verify_multiple_cards_same_user_product_success(self, card1_details,
                                                        card2_details):
        # Can be improved by accepting a list of cards instead of multiple
        # individual card
        logger.info("verifying multiple cards creation for same user and "
                    "card product successful")
        assert card1_details is not None, "No card details found"
        assert card2_details is not None, "No card details found"
        assert card1_details['last_four'] != card2_details['last_four'], \
            "last_four digits are same for multiple cards"
        assert card1_details['token'] != card2_details['token'], \
            "token are same for multiple cards"
