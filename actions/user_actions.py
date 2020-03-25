import logging

from actions.api_generic_actions import ApiGenericActions
from base.base_test import BaseTest

logger = logging.getLogger(__name__)


class UserActions(ApiGenericActions):
    def __init__(self):
        super().__init__()

    def create_user(self, user_details):
        logger.info("Creating a new user")
        user_url = self.base_url + "users"
        if user_details is not None:
            new_user = self.post(user_url, user_details)
        else:
            logger.error("Missing new user details")

        return new_user