import logging

from actions.api_generic_actions import ApiGenericActions

logger = logging.getLogger(__name__)


class FundingActions(ApiGenericActions):
    def __init__(self):
        """
         init method to create object of this class
         """
        super().__init__()
        self.funding_source_token = None
        self.funding_source_url = self.base_url + "fundingsources/program"
        self.gpaorder_token = None
        self.gpaorder_url = self.base_url + "gpaorders"

    def create_program_funding_source(self, source_details):
        """
        method to create program funding source
        :param source_details: request payload containing program src details
        :return: program_fund(json)
        """
        logger.info("Creating a  program funding source")

        if source_details is not None:
            response_msg, http_code = self.post(self.funding_source_url,
                                                source_details)

            try:
                program_fund = response_msg.json()
            except ValueError as ve:
                logger.error(
                    "Failed to convert funding source details into JSON")

            if http_code == 201:
                self.funding_source_token = program_fund['token']
            else:
                logger.error("Error in the request, HTTP code: {}"
                             .format(http_code))
        else:
            logger.error("Missing card details")

        return program_fund

    def create_gpaorder(self, gpaorder_payload):
        """
        method to create gaporder
        :param gpaorder_payload: request payload containing gaporder details
        :return: gpaorder(json)
        """
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
            else:
                logger.error("Error in the request, HTTP code: {}"
                             .format(http_code))
        else:
            logger.error("Missing gpaorder details")

        return gpaorder
