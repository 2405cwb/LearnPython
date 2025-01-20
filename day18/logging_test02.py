# author: cwb
# date: 2025/1/20
import logging
# 日志过滤器
class MyFilter(logging.Filter):
    def filter(self, record):
        # 只记录包含 "important" 的日志
        return "important" in record.getMessage()
# 创建日志记录器
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# 创建文件处理器
file_handler = logging.FileHandler("my_logger.log")
file_handler.setLevel(logging.DEBUG)

# 创建控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

# 设置日志格式
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 添加过滤器
console_handler.addFilter(MyFilter())
file_handler.addFilter(MyFilter())
# 添加处理器到记录器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 记录日志
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")