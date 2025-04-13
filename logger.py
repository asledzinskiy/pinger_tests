import logging
import sys


def setup_logger(name):
    """Sets up a logger with a specific name."""

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Set the base logging level

    # Create a formatter for the log messages
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger


default_logger = setup_logger("pinger_tests")
