import logging

from actions.api_generic_actions import ApiGenericActions

logger = logging.getLogger(__name__)


class FundingActions(ApiGenericActions):
    def __init__(self):
        super().__init__()
        self.funding_source_token = None
        self.funding_source_url = self.base_url + "fundingsources/program"
        self.gpaorder_token = None
        self.gpaorder_url = self.base_url + "gpaorders"

    def create_program_funding_source(self, source_details):
        logger.info("Creating a  program funding source")

        if source_details is not None:
            response_msg, http_code = self.post(self.funding_source_url,
                                                source_details)

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

    def create_gpaorder(self, gpaorder_payload):
        logger.info("Creating a new gpaorder")

        if gpaorder_payload is not None:
            response_msg, http_code = self.post(self.gpaorder_url,
                                                gpaorder_payload)

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
