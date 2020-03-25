import logging
from datetime import datetime

from base.base_test import BaseTest

logger = logging.getLogger(__name__)


class UtilsHelper(BaseTest):
    def time_stamp(self):
        logger.info("Creating Formatted Timestamp")
        time_stamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        return time_stamp

    def date(self):
        logger.info("Creating Formatted Date")
        current_date = datetime.now().strftime('%Y-%m-%d')
        return current_date
