# author: cwb
# date: 2025/1/21
import sys
import os

print(sys.path)

# 获取 day20 目录的绝对路径
day20_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 将 day20 目录添加到 sys.path
sys.path.append(day20_dir)
print(sys.path)
from cwb_log.MyLog import log
import logging

log('This is a debug message', logging.DEBUG)

from cwb_log.ceshi2 import main
print(main.x)