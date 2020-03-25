from actions.api_generic_actions import ApiGenericActions
from actions.user_actions import UserActions
from base.base_test import BaseTest

import logging

from base.static_config import StaticConfig

logger = logging.getLogger(__name__)


class TestSanityApi(BaseTest):
    def test_create_user_successfully(self):
        """
        Test create new user successfully
        """
        #
        # ================ CONFIGURATION ================
        #
        user_details = '{ "first_name": "Peter", "last_name": "Joe", ' \
                       '"active": true }'

        #
        # ================ ACTION ================
        #
        user_client = UserActions()
        user = user_client.create_user(user_details)

        #
        # ================ VERIFICATION ================
        #
        logger.info(user.text)


