# author: cwb
# date: 2025/1/20


#自定义迭代器

class myIterator:
    def __init__(self,s,e):
        self.current = s
        self.end=e
    def __next__(self):
        if self.current< self.end:
            self.current += 1
            return self.current-1
        else :
            return StopIteration
    def __iter__(self):
        return self
# 使用迭代器

itor =  myIterator(10,12)

print(next(itor))

class MyIterator01:
    def __init__(self,data):
        self.data = data
        self.index = 0
    def __next__(self):
        len1 = len(self.data)
        if self.index < len1:
            data = self.data[self.index]
            self.index+=1
            return data
        else:
            raise StopIteration("超出索引")
    def __iter__(self):
        return self



data1 = MyIterator01([1,2,3,2,1,3,6,3])

for i in data1:
    print(i)
try:
    for i in range(10):
        print(next(data1))
except Exception as error:
    print(error,"所有异常捕捉")
else:
    print("没有捕获到异常")
finally:
    print("结束!")

from collections.abc import Iterator, Iterable
print(isinstance(data1,Iterator))
print(isinstance(data1,Iterable))


#isinstance() 用于检查对象是否是指定类（或类型）的实例，或者是否是该类的子类的实例。
#它支持检查多个类型（通过元组）。
# 列表是可迭代的，但不是迭代器
data1 = [1, 2, 3]
print(isinstance(data1, Iterable))  # 输出: True
print(isinstance(data1, Iterator))  # 输出: False

# 迭代器是可迭代的，同时也是迭代器
data2 = iter(data1)
print(isinstance(data2, Iterable))  # 输出: True
print(isinstance(data2, Iterator))  # 输出: True
