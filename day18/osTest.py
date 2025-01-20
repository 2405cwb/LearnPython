# author: cwb
# date: 2025/1/20

import  os

# 获取当前工作目录
print(os.getcwd())
# os.chdir('..')
print(os.getcwd())

# os.mkdir('test')
# os.makedirs("test\\aaa\ddd")
# os.removedirs()
# os.rmdir()
#返回当前目录
os.curdir

print( os.listdir(".."))

# 删除文件
# os.remove()

# 获取文件信息
stat=os.stat("osTest.py")
print( stat)

print(os.sep)
# 换行符
print(os.linesep)

# 路径分隔符
print(os.pathsep)

# 执行shell命令
os.system("cd ..")

# 环境变量
print(os.environ)

os.path.abspath('..')
#绝对路径 和  文件名
os.path.split('')

#文件夹名称
print( os.path.dirname(__file__),"文件夹名称")

