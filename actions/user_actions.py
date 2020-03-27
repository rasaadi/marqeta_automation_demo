import logging

from actions.api_generic_actions import ApiGenericActions

logger = logging.getLogger(__name__)


class UserActions(ApiGenericActions):
    def __init__(self):
        super().__init__()
        self.user_token = None
        self.user_url = self.base_url + "users"

    def create_user(self, user_details):
        logger.info("Creating a new user")

        if user_details is not None:
            response_msg, http_code = self.post(self.user_url, user_details)

            try:
                new_user = response_msg.json()
            except ValueError as ve:
                logger.error("Failed to convert user details into JSON")

            if http_code == 201:
                self.user_token = new_user['token']
            else:
                logger.error("Error in the request, HTTP code: {}"
                             .format(http_code))
        else:
            logger.error("Missing card details")

        return new_user
