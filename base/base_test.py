import logging

logger = logging.getLogger(__name__)


class BaseTest:

    @classmethod
    def setup_class(cls):
        """
        setup_class() will be invoked for the given class (which
        usually contains tests) at the beginning.
        """
        logger.info("<<<<<<<<<<<<<<<<<<<<<<START CLASS>>>>>>>>>>>>>>>>>>>>>>")
        logger.info("Class Name: {0}".format(cls.__name__))

    @classmethod
    def teardown_class(cls):
        """
        teardown_class() will be invoked for the given class (which
        usually contains tests) at the end.
        """
        logger.info("<<<<<<<<<<<<<<<<<<<<<<END CLASS>>>>>>>>>>>>>>>>>>>>>>")

    def setup_method(self, method):
        """
        setup_method() will be invoked for every test method of a class at
        the beginning.
        """
        logger.info("<<<<<<<<<<<<<<<<<<<<<<START TEST>>>>>>>>>>>>>>>>>>>>>>")
        logger.info("Test Name: {0}".format(method.__name__))

    def teardown_method(self, method):
        """
        teardown_method() will be invoked for every test method of a class
        at the end.
        """
        logger.info("<<<<<<<<<<<<<<<<<<<<<<END TEST>>>>>>>>>>>>>>>>>>>>>>")
