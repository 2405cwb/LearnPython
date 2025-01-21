# author: cwb
# date: 2025/1/21
import logging
from atm_module.logger import log

def cwb_log(name, msg):
    # 创建一个 Logger 实例
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # 设置日志级别

    # 创建一个文件处理器
    file_handler = logging.FileHandler(name, mode='a')
    file_handler.setLevel(logging.DEBUG)

    console_handel = logging.StreamHandler()
    console_handel.setLevel(logging.DEBUG)

    # 创建一个格式化器
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_handler.setFormatter(formatter)
    console_handel.setFormatter(formatter)


    # 将处理器添加到 Logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handel)

    # 调用 log 函数
    log(logger, msg)
