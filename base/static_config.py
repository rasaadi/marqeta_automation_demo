import logging
import os

logger = logging.getLogger(__name__)


class StaticConfig:

    # System agnostic PATH info
    ABS_PATH_TO_BASE_TEST = os.path.dirname(os.path.abspath(__file__))
    ABS_PATH_TO_ROOT = os.path.dirname(ABS_PATH_TO_BASE_TEST)

    REPORT_PATH = os.path.join(ABS_PATH_TO_ROOT, "reports/")
    RESOURCE_PATH = os.path.join(ABS_PATH_TO_ROOT, "resources/")

