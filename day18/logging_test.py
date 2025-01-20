# author: cwb
# date: 2025/1/20
'''
记录日志: 将程序运行时的信息、警告、错误等记录到文件或控制台。

分级日志: 支持不同级别的日志（如 DEBUG、INFO、WARNING、ERROR、CRITICAL）。

灵活配置: 可以配置日志的格式、输出位置、级别等。

多模块支持: 可以为不同的模块设置不同的日志记录器。
'''
import os

'''
logging 模块定义了以下日志级别（从低到高）：

级别	数值	描述
DEBUG	10	调试信息，通常用于开发阶段。
INFO	20	程序正常运行时的信息。
WARNING	30	警告信息，表示潜在的问题。
ERROR	40	错误信息，表示程序中的错误。
CRITICAL	50	严重错误，可能导致程序崩溃。
默认情况下，logging 只会记录 WARNING 及以上级别的日志。
'''

import logging
print( os.getcwd())

# 配置日志级别、格式和输出文件
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log"

    #,filemode = "w"  # 覆盖模式
)

# 记录日志
logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")


# 记录日志
logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")