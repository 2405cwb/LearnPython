# author: cwb
# date: 2025/1/15

Ages = [1, 2, 3, 4, 5, 6, 7, 8]

time = range(1000)

# 增
Ages.append(10)
Ages.append(3)
Ages.insert(3, 22)
# 删
Ages.remove(3)
data = Ages.pop(0)
print("data is ", data)
Ages.sort()
del Ages[5]
# 改
Ages[0] = 100
# 查
print(Ages)
# print(time[1:3])
print(Ages[5:3:-1])

print(Ages[1:-1:3])


# count方法
print("-------------------METHOD-------------------")
print(Ages.count(1))
# extend
Ages1 = [10, 100, 1000, 10000, 5555, 9999]
Ages.extend(Ages1)
print(Ages)

indexTemp = Ages.index(10)
print(indexTemp)