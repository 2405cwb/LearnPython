# author: cwb
# date: 2025/2/17


import io
import json
import sys
import pickle
from jsonHelper import writeJson, readJson,myJson # 从 jsonHelper 导入 writeJson 和 readJson
 
fileName = 'json_file.json'
fileName1 = 'json_file1.json'
# 定义一个示例对象
data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
data1 = {'name': '张三', 'age': 32, 'city': '上海'}
# 解决中文乱码问题   
# 使用新的writeJson和readJson函数
writeJson(fileName, data)
readJson(fileName)

writeJson(fileName1, data1)
readJson(fileName1)

data1 = {'name': '程文博', 'age': 30, 'city': 'New York'}
#使用json序列化
writeJson(fileName, data)
readJson(fileName)

myJson = myJson(fileName1, data1)
myJson.writeJson()
myJson.readJson()