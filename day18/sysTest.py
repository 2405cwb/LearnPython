# author: cwb
# date: 2025/1/20
import os
import sys

print("执行",sys.argv.append(1))
sys.argv #传入python解释器的参数

if sys.argv[1] == '3':
    print('捕捉到了参数3')

print(sys.version)
print( sys.maxsize)

# 返回模块的搜索路径  初始化时 使用PYTHONPATH环境变量的值
print(sys.path)
#返回操作系统平台名称
print(sys.platform)

var = sys.stdin.readline()[:-1]
print(var)
sys.stdout.write('please:')

if sys.platform == 'win32':
    os.system('dir')
else:
    os.system('ls')

# 退出
sys.exit()