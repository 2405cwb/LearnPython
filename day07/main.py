# author: cwb
# date: 2025/1/15

# 文件操作

file = open("小重山", 'r', encoding='utf-8')
txt = file.read(10)
txt2 = file.readline(2)
print(txt2)

wFile = open("ttt.txt", 'w', encoding='utf-8')
wFile.write("cccc")
wFile.write("acccc223")
wFile.writelines("测试\r\nddda")
wFile.writelines("测试")
file.close()
wFile.close()
