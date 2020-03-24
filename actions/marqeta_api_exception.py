class MarqetaApiException(Exception):
    """
    Exception (common) raised for failures related to Marqeta API
    """
    pass


class CardException(MarqetaApiException):
    """
    Exception raised for failures related to Card creation API
    """
    pass


class TransactionException(MarqetaApiException):
    """
       Exception raised for failures related to Transaction API
       """
    pass
