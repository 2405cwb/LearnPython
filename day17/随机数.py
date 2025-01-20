# author: cwb
# date: 2025/1/20
import random

# 生成随机浮点数
print(random.random())  # 输出: [0.0, 1.0) 之间的随机浮点数

# 生成随机整数
print(random.randint(1, 10))  # 输出: [1, 10] 之间的随机整数

# 生成随机浮点数
print(random.uniform(1.0, 10.0))  # 输出: [1.0, 10.0] 之间的随机浮点数

# 从序列中随机选择一个元素
my_list = [1, 2, 3, 4, 5]
print(random.choice(my_list))  # 输出: 随机选择一个元素

# 打乱序列
random.shuffle(my_list)
print(my_list)  # 输出: 打乱后的序列

# 从序列中随机选择 k 个不重复的元素
print(random.sample(my_list, 3))  # 输出: 随机选择 3 个不重复的元素