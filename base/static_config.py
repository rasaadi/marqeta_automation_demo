import logging
import os

logger = logging.getLogger(__name__)


class StaticConfig:
    # Sandbox Details:
    SANDBOX_BASE_URL = "https://sandbox-api.marqeta.com/v3/"

    '''
    Enable/Disable this block of code if you want to run code directly(not 
    to deal with env) with your own Application token and Master Token
    '''
    # APP_TOKEN = 'placeholder'
    # MASTER_TOKEN = 'placeholder'

    ''''
    Enable/Disable this block of the code if the project is intended to run in 
    Jenkins or GitHub Workflow or use System Environment variable to parse 
    APP_TOKEN and 
    MASTER_TOKEN
    '''
    try:
        APP_TOKEN = str(os.getenv("APP_TOKEN")).strip()
        MASTER_TOKEN = str(os.getenv("MASTER_TOKEN")).strip()

    except AttributeError as AE:
        logger.exception("Exception occurred while parsing Env variable: {0}"
                         .format(AE))
