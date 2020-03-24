import logging
import requests
import time

from base.base_test import BaseTest
from base.static_config import StaticConfig
from actions.marqeta_api_exception import (MarqetaApiException,
                                           CardException, TransactionException)

logger = logging.getLogger(__name__)


class ApiGenericActions(BaseTest):
    def __init__(self):
        """
        init method to create object of the class
        """
        self.session = requests.Session()
        self.base_url = StaticConfig.SANDBOX_BASE_URL
        self.headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }
        self.payload = None
        self.data = None
        self.auth = None

    def get(self, url):
        """
        generic GET method to perform API GET request
        :param url:
        :return:
        """
        logger.info("Executing GET request: {}".format(url))
        try:
            response = self.session.get(url, headers=self.headers)
            time.sleep(5)
        except requests.exceptions.RequestException as re:
            logger.error("GET request execution failed: {}".format(re))
        else:
            if response.status_code == 200:
                return response
            else:
                raise MarqetaApiException("Marqeta api GET request error, "
                                          "response content: {}".format(
                    response.text))

    def post(self, url, data=None, auth=None):
        """
        generic POST method to perform API POST request
        :param url:
        :param payload:
        :param data:
        :return:
        """
        logger.info("Executing POST request: {}".format(url))
        self.data = data
        self.auth = auth
        try:
            if auth is not None:
                response = self.session.post(url, headers=self.headers,
                                             data=self.data, auth=self.auth)
            else:
                response = self.session.post(url, headers=self.headers,
                                             data=self.data)
            time.sleep(5)
        except requests.exceptions.RequestException as re:
            logger.error("POST request execution failed: {}".format(re))
        else:
            if response.status_code == 200:
                return response
            else:
                raise MarqetaApiException("Marqeta api POST request error, "
                                          "response content: {}".format(
                    response.text))

    def create_user(self, user_details, auth_token):
        logger.info("Creating a new user")
        user_url = self.base_url + "users"
        if user_details is not None:
            new_user = self.post(user_url, user_details, auth_token)
        else:
            logger.error("Missing new user details")

        return new_user
