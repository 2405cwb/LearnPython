# author: cwb
# date: 2025/1/20

import configparser

# 创建 ConfigParser 对象
config = configparser.ConfigParser()

# 读取配置文件
config.read('config.ini')

# 获取配置值
server_ip = config['DEFAULT']['server_ip']
port = config['DEFAULT'].getint('port')  # 获取整数类型的值

print(f"Server IP: {server_ip}, Port: {port}")

#使用 sections() 方法获取所有节的列表。
sections = config.sections()
print("Sections:", sections)
#使用 items() 方法获取某个节中的所有键值对。
database_items = config.items('database')
print("Database items:", database_items)
# 检查节是否存在
if config.has_section('database'):
    print("Section 'database' exists.")

# 检查键是否存在
if config.has_option('database', 'host'):
    print("Key 'host' exists in section 'database'.")

#使用 add_section() 和 set() 方法添加节和键值对。
# 添加新节
config.add_section('logging')

# 添加键值对
config.set('logging', 'level', 'DEBUG')
config.set('logging', 'file', 'app.log')

# 写入配置文件
with open('config.ini', 'w') as configfile:
    config.write(configfile)
'''
(2) 删除节或键
使用 remove_section() 和 remove_option() 方法删除节或键。
'''
# 删除键
config.remove_option('logging', 'file')

# 删除节
config.remove_section('logging')

# 写入配置文件
with open('config.ini', 'w') as configfile:
    config.write(configfile)

'''
4. 处理默认值
DEFAULT 节是一个特殊的节，它的键值对会被其他节继承。
'''
# 获取 database 节的 host
host = config['database']['host']
print("Database host:", host)

# 获取 database 节的 server_ip（继承自 DEFAULT 节）
server_ip = config['database']['server_ip']
print("Database server IP:", server_ip)

'''
5. 高级用法
(1) 插值（Interpolation）
configparser 支持插值，可以在值中引用其他键的值。


[DEFAULT]
base_dir = /var/log
log_file = %(base_dir)s/app.log


读取
log_file = config['DEFAULT']['log_file']
print("Log file path:", log_file)


configparser 支持两种插值方式：

BasicInterpolation（默认）:

使用 %(key)s 语法。

只能引用当前节或 DEFAULT 节中的键。

ExtendedInterpolation（扩展插值）:

使用 ${section:key} 或 ${key} 语法。

可以跨节引用键。
'''

# (2) 自定义插值
# 可以通过继承 configparser.BasicInterpolation 或 configparser.ExtendedInterpolation 实现自定义插值。

# from configparser import ConfigParser, ExtendedInterpolation
#
# config = ConfigParser(interpolation=ExtendedInterpolation())
# config.read('config.ini')
#
# log_file = config['DEFAULT']['log_file']
# print("Log file path:", log_file)