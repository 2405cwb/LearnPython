# author: cwb
# date: 2025/1/21
import logging


def set_logger(log_file:str="app.log",level:int=logging.DEBUG) -> logging.Logger:
    """
      配置并返回一个日志记录器。

    :param log_file: 日志文件名
    :param level: 日志级别
    :return: 配置好的日志记录器
    """
    logging.basicConfig(filename=log_file, level=level)
    return logging.getLogger(__name__)


def log(message:str,level:int=logging.INFO):
    """
    记录日志
    :param message: 日志消息
    :param level: 日志级别
    """
    logger = set_logger()
    if level == logging.INFO:
        logger.info(message)
    elif level == logging.ERROR:
        logger.error(message)
    elif level == logging.WARNING:
        logger.warning(message)
    elif level == logging.DEBUG:
        logger.debug(message)
    elif level == logging.CRITICAL:
        logger.critical(message)
    else:
        logger.info(message)

