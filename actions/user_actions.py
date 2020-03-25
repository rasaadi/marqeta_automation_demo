import logging

from actions.api_generic_actions import ApiGenericActions

logger = logging.getLogger(__name__)


class UserActions(ApiGenericActions):
    def __init__(self):
        super().__init__()
        self.user_token = None

    def create_user(self, user_details):
        logger.info("Creating a new user")
        user_url = self.base_url + "users"
        if user_details is not None:
            new_user = self.post(user_url, user_details).json()
            self.user_token = new_user['token']
        else:
            logger.error("Missing new user details")

        return new_user