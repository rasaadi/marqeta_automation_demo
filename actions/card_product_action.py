import logging

from actions.api_generic_actions import ApiGenericActions

logger = logging.getLogger(__name__)

class CardProductActions(ApiGenericActions):

    def __init__(self):
        """
        init method to create object of this class
        """
        super().__init__()
        self.product_token = None
        self.product_url = self.base_url + "cardproducts"

    def create_card_product(self, card_product_details):
        """
        method to create card products
        :param card_product_details: request payload containing product details
        :return: card_product(json)
        """
        logger.info("Creating a new card product")

        if card_product_details is not None:
            response_msg, http_code = self.post(self.product_url,
                                                card_product_details)

            try:
                card_product = response_msg.json()
            except ValueError as ve:
                logger.error("Failed to convert card product details into "
                             "JSON")

            if http_code == 201:
                self.product_token = card_product['token']
            else:
                logger.error("Error in the request, HTTP code: {}"
                             .format(http_code))
        else:
            logger.error("Missing card details")

        return card_product