import logging

from base.base_test import BaseTest

logger = logging.getLogger(__name__)


class CardVerifications(BaseTest):
    def verify_card_creation_successful(self, card_api_response,
                                        card_resources):
        logger.info("verifying card creation is successful")
        assert card_api_response is not None, "No card object details found"
        assert card_api_response['token'] is not None, "No card token found"
        assert card_api_response['user_token'] == card_resources.user_token, \
            "User token mismatch"
        assert card_api_response['card_product_token'] == card_resources.\
            card_product_token, "Card product token mismatch"
