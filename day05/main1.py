#!/user/bin/env python
# author: Administrator
# date: 2025/1/15
class People:
    Name = ""
    Age = 0

    # 初始化方法
    def __init__(self, name, age):
        self.Name = name
        self.Age = age

    def __str__(self):
        msg = '''
        -----------------info of %s ----------------------
        Name:%s
        Age:%s
        ''' % (self.Name, self.Name, self.Age)
        return msg


for i in range(10):
    p = People("name" + str(i), i)
    print(p)

# 扩展
