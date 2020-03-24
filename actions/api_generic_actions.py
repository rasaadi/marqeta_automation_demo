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
        # Netsense.__init__(self, pod_name)
        self.session = requests.Session()
        self.base_url = StaticConfig.SANDBOX_BASE_URL
        self.headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }
        self.payload = None
        self.data = None

    def get(self, url):
        """
        generic GET method to perform API GET
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
                                          "response content: {}".format(response.text))

    def post(self, url, payload=None, data=None):
        logger.info("Executing POST request: {}".format(url))
        self.payload = payload
        self.data = data
        try:
            response = self.session.post(url, headers=self.headers,
                                         json=self.payload, data=self.data)
            time.sleep(5)
        except requests.exceptions.RequestException as re:
            logger.error("POST request execution failed: {}".format(re))
        else:
            if response.status_code == 200:
                return response
            else:
                raise MarqetaApiException("Marqeta api POST request error, "
                                          "response content: {}".format(response.text))