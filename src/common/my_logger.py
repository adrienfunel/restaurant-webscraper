import os
import logging


def set_logger():
    """
    Function to set up the loggers parameters.
    :return: N/A
    """
    log_dir = os.path.abspath('../logs')
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)

    log_level = 'INFO'
    logging_format = '%(asctime)s:%(name)s:%(message)s'

    file_handler = logging.FileHandler(os.path.join(log_dir, 'scraper_logs.log'))
    file_handler.setFormatter(logging.Formatter(logging_format))
    file_handler.setLevel(log_level)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter(logging_format))

    logger = logging.getLogger()
    logger.setLevel(log_level)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    logger.info("Logging started in {}\n".format(log_dir))