"""
This module provides a function to configure a custom logger
for a specific class. The logger logs error messages in a file
of log in a logs folder.
"""

import logging
import os

def setup_logger(class_name):
    """
    Sets a custom logger for the specified class.
    Args:
        class_name (str): The class name for which the logger will be configured.
    Returns:
        logging.Logger: The configured logger.
    """
    # Create to the carpet of logs and no exist
    log_directory = "logs"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    # Configure a custom logger
    logger = logging.getLogger(class_name)
    logger.setLevel(logging.ERROR)
    # Create a handler for the log file
    file_handler = logging.FileHandler(os.path.join(log_directory, f"{class_name.lower()}.log"))
    file_handler.setLevel(logging.ERROR)
    # Log format for the file
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    # Add the handler to the custom logger
    logger.addHandler(file_handler)
    return logger
