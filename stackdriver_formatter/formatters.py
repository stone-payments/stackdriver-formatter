"""app.formatters

Module that contains the log formatters of our app.
"""
from pythonjsonlogger import jsonlogger

class StackDriverJsonFormatter(jsonlogger.JsonFormatter):
    """StackDriverJsonFormatter is a child of a JsonFormatter that adds
       logs to StackDriver with the correct severity level."""

    def __init__(self, *args, fmt="%(levelname) %(message)", **kwargs):
        jsonlogger.JsonFormatter.__init__(self, fmt=fmt, *args, **kwargs)

    def process_log_record(self, log_record):
        log_record['severity'] = log_record['levelname']
        del log_record['levelname']
        return super(StackDriverJsonFormatter, self).process_log_record(log_record)
