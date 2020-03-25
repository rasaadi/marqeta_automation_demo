import logging

from actions.api_generic_actions import ApiGenericActions

logger = logging.getLogger(__name__)


class CardActions(ApiGenericActions):
    def __init__(self):
        super().__init__()
        self.product_token = None
        self.card_token = None
        self.funding_source_token = None

    def create_card_product(self, card_product_details):
        logger.info("Creating a new card product")

        product_url = self.base_url + "cardproducts"
        if card_product_details is not None:
            response_msg, http_code = self.post(product_url,
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

        card_url = self.base_url + "cards"
        if card_details is not None:
            response_msg, http_code = self.post(card_url, card_details)

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

    def create_program_funding_source(self, source_details):
        logger.info("Creating a  program funding source")

        source_url = self.base_url + "fundingsources/program"
        if source_details is not None:
            response_msg, http_code = self.post(source_url, source_details)

            try:
                new_program_fund = response_msg.json()
            except ValueError as ve:
                logger.error(
                    "Failed to convert funding source details into JSON")

            if http_code == 201:
                self.funding_source_token = new_program_fund['token']
            elif http_code == 409:
                logger.error(
                    "Request already associated with a different payload")
            else:
                logger.error("Invalid fields detected")
        else:
            logger.error("Missing card details")

        return new_program_fund
