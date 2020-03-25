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
            new_product = self.post(product_url, card_product_details)
            self.product_token = new_product['token']
        else:
            logger.error("Missing card product details")

        return new_product

    def create_card(self, card_details):
        logger.info("Creating a  new card product")

        card_url = self.base_url + "cards"
        if card_details is not None:
            new_card = self.post(card_url, card_details)
            self.product_token = new_card['token']
        else:
            logger.error("Missing card details")

        return new_card

    def create_program_funding_source(self, source_details):
        logger.info("Creating a  program funding source")

        source_url = self.base_url + "fundingsources/program"
        if source_details is not None:
            new_program_fund = self.post(source_url, source_details)
            # self.funding_source_token = new_program_fund['token']
        else:
            logger.error("Missing funding source details")

        return new_program_fund
