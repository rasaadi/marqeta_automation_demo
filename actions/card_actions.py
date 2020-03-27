import logging

from actions.api_generic_actions import ApiGenericActions

logger = logging.getLogger(__name__)


class CardActions(ApiGenericActions):
    def __init__(self):
        super().__init__()
        self.product_token = None
        self.product_url = self.base_url + "cardproducts"
        self.card_token = None
        self.card_url = self.base_url + "cards"

    def create_card_product(self, card_product_details):
        logger.info("Creating a new card product")

        if card_product_details is not None:
            response_msg, http_code = self.post(self.product_url,
                                                card_product_details)

            try:
                new_product = response_msg.json()
            except ValueError as ve:
                logger.error("Failed to convert card product details into "
                             "JSON")

            if http_code == 201:
                self.product_token = new_product['token']
            elif http_code == 409:
                logger.error(
                    "Token already associated with a different payload")
            else:
                logger.error("User input error/Bad request")
        else:
            logger.error("Missing card details")

        return new_product

    def create_card(self, card_details):
        logger.info("Creating a  new card")

        if card_details is not None:
            response_msg, http_code = self.post(self.card_url, card_details)

            try:
                new_card = response_msg.json()
            except ValueError as ve:
                logger.error("Failed to convert card details into JSON")

            if http_code == 201:
                self.card_token = new_card['token']
            elif http_code == 409:
                logger.error(
                    "Token already associated with a different payload")
            else:
                logger.error("User input error/Bad request")
        else:
            logger.error("Missing card details")

        return new_card
