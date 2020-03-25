import logging
import os

logger = logging.getLogger(__name__)


class StaticConfig:

    # Sandbox Details:
    SANDBOX_BASE_URL = "https://sandbox-api.marqeta.com/v3/"
    APP_TOKEN = "5b4be8a7-c908-4840-8c57-3b40253e7831"

    # System agnostic PATH info
    ABS_PATH_TO_BASE_TEST = os.path.dirname(os.path.abspath(__file__))
    ABS_PATH_TO_ROOT = os.path.dirname(ABS_PATH_TO_BASE_TEST)

    REPORT_PATH = os.path.join(ABS_PATH_TO_ROOT, "reports/")
    RESOURCE_PATH = os.path.join(ABS_PATH_TO_ROOT, "resources/")
