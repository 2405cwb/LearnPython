# 普通函数定义
def add(a, b):
    return a + b


# 默认参数函数
def getArea(r, pi=3.1415926):
    area = r * r * pi
    return area

# 多个返回值的函数
def multReturnMethon(a:int,b:int):
    return a+10,b*b
multResult=multReturnMethon(10,10000)
print('可变参数:',multResult)

# 可变参数函数 和关键字可变参数  及参数备注
def method11(*args:float,**kwargs:{str,float})->float:
    sum = 0
    for i in args:
        sum+=i
    for key,value in kwargs.items():
        print("key是%s,值是"%(key),value)
    return sum

print("圆的面积是:", getArea(10))
print(add(1, 2))
result =method11(1,2,3,4,5,name=1,data=10)
print("result:",result)

#特殊函数
##匿名函数
###lambda
square = lambda a:a**2
print("lambda",square(10))
# 在列表排序中使用
data = [(1, 3), (4, 1), (2, 2)]
data.sort(key= lambda x:x[1])

#生成器函数 yield
###
# 使用 yield 关键字定义生成器函数。
# 生成器函数返回一个生成器对象，支持惰性求值（按需生成值）。
# 适合处理大量数据或无限序列。
###
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 使用生成器生成斐波那契数列
fib = fibonacci()
for _ in range(10):
    print(next(fib))
with open('large_file.txt','w',encoding='utf-8') as d:
    for i in range(100):
        d.write('数字：'+str(i)+'\n')

def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()


    # 使用生成器逐行读取文件
for line in read_large_file('large_file.txt'):
        print(line)
#装饰器函数
###
#装饰器是一种高阶函数，用于修改或增强其他函数的行为。
#使用 @ 符号将装饰器应用到函数上。
###
def logger(func):
    """记录函数调用的装饰器"""
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(3, 5))  # 输出: 调用函数: add \n 8
#递归函数
def factorial(n):
    """计算阶乘"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 输出: 120
#闭包函数
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
print(closure(5))  # 输出: 15