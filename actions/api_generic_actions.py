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
        init method to create object of this class
        """
        self.base_url = StaticConfig.SANDBOX_BASE_URL
        self.headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
        }
        self.app_token = StaticConfig.APP_TOKEN
        self.master_token = StaticConfig.MASTER_TOKEN

    def get(self, url):
        """
        generic GET method to perform API GET request
        :param url: API end point URL
        :return: response, status_code
        """
        logger.info("Executing GET request: {}".format(url))
        try:
            response = requests.get(url, headers=self.headers,
                                    auth=(self.app_token, self.master_token))
            time.sleep(5)
        except requests.exceptions.RequestException as re:
            logger.error("GET request execution failed: {}".format(re))
        else:
            if response.status_code != 500:
                return response, response.status_code
            else:
                raise MarqetaApiException("Marqeta api GET request error, "
                                          "response content: {}".format(
                                                                response.text))

    def post(self, url, data=None):
        """
        generic POST method to perform API POST request
        :param url: API end point URL
        :param data: Request body
        :return: response, status_code
        """
        logger.info("Executing POST request: {}".format(url))
        try:
            if data is not None:
                response = requests.post(url, headers=self.headers,
                                         data=data, auth=(self.app_token,
                                                          self.master_token))
            time.sleep(2)
        except requests.exceptions.RequestException as re:
            logger.error("POST request execution failed: {}".format(re))
        else:
            if response.status_code != 500:
                return response, response.status_code
            else:
                raise MarqetaApiException("Marqeta api POST request error, "
                                          "response content: {}".format(
                                                                response.text))
