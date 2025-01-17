# author: cwb
# date: 2025/1/17

#装饰器

#装饰器用于修改或扩展函数或方法的行为，而无需修改其原始代码，装饰器的核心思想时高阶函数和闭包
#装饰器的本质是一个函数，它接受一个函数作为参数，并返回一个新的函数

# 简单装饰器

def my_decorator(method):
    def wrapper():
        print("函数执行：")
        method()
        print("函数执行完毕.")
    return wrapper


@my_decorator
def say_hello():
    print("hello!")

say_hello()



import time
# 装饰器推导

def sqrt(x):
    time.sleep(0.1)
    return x*x
# 函数调用函数

def method(func,x):
    print(f"{func.__name__}函数开始")
    func(x)
    print("函数结束")

method(sqrt,10)



# 匹配多个方法
def method2(func):
    def wrapper(*args,**kwargs):
        print(f'{func.__name__}开始执行')
        time_start =  time.time()
        result =  func(*args,**kwargs)
        time_end = time.time()
        print(f'{func.__name__}执行完毕。执行时间是{time_end-time_start}')
        return  result
    return wrapper


decoratorMethod =  method2(sqrt)
decoratorMethod(22)
#进一步优化
method2 =  method2(sqrt)
method2(858522)

#使用关键词语法糖
def method3(func):
    def wrapper(*args,**kwargs):
        print(f'{func.__name__}开始执行')
        time_start =  time.time()
        result =  func(*args,**kwargs)
        time_end = time.time()
        print(f'{func.__name__}执行完毕。执行时间是{time_end-time_start}')
        return result
    return wrapper
@method3
def methodPage(x):
    return sqrt(x)
value =  methodPage(199889)
print('最终结果是',value)