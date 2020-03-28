import logging
import os

logger = logging.getLogger(__name__)


class StaticConfig:
    # Sandbox Details:
    SANDBOX_BASE_URL = "https://sandbox-api.marqeta.com/v3/"
    APP_TOKEN = 'placeholder'
    MASTER_TOKEN = 'placeholder'

    ''''
    Enable this block of the code if the project is intended to run in 
    Jenkins or use System Environment variable to parse APP_TOKEN and 
    MASTER_TOKEN
    '''
    # try:
    #     APP_TOKEN = str(os.getenv("APP_TOKEN")).strip()
    #     MASTER_TOKEN = str(os.getenv("MASTER_TOKEN")).strip()
    #
    # except AttributeError as AE:
    #     logger.exception("Exception occurred while parsing Env variable: {0}"
    #                      .format(AE))
