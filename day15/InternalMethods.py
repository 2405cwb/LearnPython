# author: cwb
# date: 2025/1/17
# 内置方法学习
# 输出
import time
print("ddd")

# 输入
# a = input("请输入")
abs(-1)


# enumerate() 返回枚举对象
for index , value in enumerate(['a','b','c']):
    print(index,":",value)

# zip 将多个可迭代对象打包成元组
for a,b in zip([1,2,3],['a','b', 'c']):
    print(a,b)
#type
# isinstance() 检查对象是否时某个类的实例

print(isinstance(10,float))
print(isinstance(10,int))
#id 返回对象的唯一标识符 内存地址

print(id(10))

# dir 返回对象的属性和方法列表

print(dir([]))

# sorted() 返回排序后的列表
sorted([3,1,2])

#反序
reversed([1,2,3])

#帮助信息
data =  help(print())
print(type(data))
print(data)
#动态执行  执行字符串形式的表达式
result = eval("9+9")
#执行字符串形式的代码
exec("print('hello,world')")



# 直接执行代码
start_time = time.time()
for _ in range(100000):
    x = 1 + 2
end_time = time.time()
print(f"直接执行时间: {end_time - start_time:.6f} 秒")

# 使用 eval 动态执行
start_time = time.time()
for _ in range(100000):
    eval("1 + 2")
end_time = time.time()
print(f"eval 执行时间: {end_time - start_time:.6f} 秒")