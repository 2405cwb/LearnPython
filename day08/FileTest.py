# author: cwb
# date: 2025/1/16
import sys ,time, random


file = open("file.txt", 'w', encoding="utf-8")
# r+ 读写模式  w+ 写读模式 a+ 追加模式
for i in range(100):
    sys.stdout.write('-')
sys.stdout.tell()
for i in range(100):
    strMsg = "".join( [str(random.randint(i, 1000)), ','])
    file.write(strMsg)
    file.flush()
    sys.stdout.write('*')
    sys.stdout.flush()


file.flush()

file.close()

with open('file1.txt','w') as f, open('file1.txt', 'r') as r:
    f.write('test')
    f.flush()
    str = r.read()
    print(str)
print("\n文件操作结束")