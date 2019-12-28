class InitializationException(Exception):
    """Exception raised when something occurs that makes the app
       uninintializable."""

class CouldNotSetLogLevel(InitializationException):
    """Exception raised when a log level couldn't be set."""

class CouldNotSetStreamHandler(InitializationException):
    """Exception raised when a stream handler couldn't be set."""
