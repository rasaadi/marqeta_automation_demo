import logging

from actions.api_generic_actions import ApiGenericActions

logger = logging.getLogger(__name__)


class GpaorderActions(ApiGenericActions):
    def __init__(self):
        super().__init__()
        self.gpaorder_token = None
        self.url = self.base_url + "gpaorders"

    def create_gpaorder(self, gpaorder_payload):
        logger.info("Creating a new gpaorder")

        if gpaorder_payload is not None:
            response_msg, http_code = self.post(self.url, gpaorder_payload)

            try:
                gpaorder = response_msg.json()
            except ValueError as ve:
                logger.error("Failed to convert gpaorder details into JSON")

            if http_code == 201:
                self.gpaorder_token = gpaorder['token']
            elif http_code == 409:
                logger.error(
                    "Request already processed with a different payload")
            elif http_code == 422:
                logger.error("Rule violations or declined transactions from "
                             "funding source")
            else:
                logger.error("User input error/Bad request")
        else:
            logger.error("Missing gpaorder details")

        return gpaorder
