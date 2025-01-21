# author: cwb
# date: 2025/1/21
# 程序执行入口
'''
import sys
import os
from pathlib import Path
# 将项目根目录添加到 sys.path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

# 获取 day20 目录的绝对路径
# ATM_dir = os.path.join( os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# # 将 day20 目录添加到 sys.path
# sys.path.append(ATM_dir)
print(sys.path)
'''



from atm_module.cwb_test import cwb_log

cwb_log('log.txt','cccccc')

