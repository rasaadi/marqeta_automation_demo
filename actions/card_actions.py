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
        logger.info("Creating a  new card product")

        product_url = self.base_url + "cardproducts"
        if card_product_details is not None:
            new_product = self.post(product_url, card_product_details).json()
            self.product_token = new_product['token']
        else:
            logger.error("Missing card product details")

        return new_product

    def create_card(self, card_details):
        logger.info("Creating a  new card")

        card_url = self.base_url + "cards"
        if card_details is not None:
            response_msg, http_code = self.post2(card_url, card_details)

            try:
                new_card = response_msg.json()
            except ValueError as ve:
                logger.error("Failed to convert card details into JSON")

            if http_code == 201:
                self.product_token = new_card['token']
            elif http_code == 409:
                logger.error(
                    "Token already associated with a different payload")
            else:
                logger.error("User input error/Bad request")
        else:
            logger.error("Missing card details")

        return response_msg.json()

    def create_program_funding_source(self, source_details):
        logger.info("Creating a  program funding source")

        source_url = self.base_url + "fundingsources/program"
        if source_details is not None:
            new_program_fund = self.post(source_url, source_details).json()
            self.funding_source_token = new_program_fund['token']
        else:
            logger.error("Missing funding source details")

        return new_program_fund
