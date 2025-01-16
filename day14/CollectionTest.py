# 列表 可变
a = [1,2,3]
# 列表
b = list((1,3))
c = list([222,333])
#元祖 不可变 两个元祖可加
tu = (3,4)
print(type(tu))
tu1 = tuple([1, 2])
print(tu1)
# 集合
d = {'a','b'}
print(type( a))
print(type(b))
print(type(c))
print(d)
# python中的集合
# set 可变集合
a1 = {1,2,3,4,5}
a2 = set([1,2,3,4,5, 6,9])
a3 = set((1,2))
a1.add(6)
a1.remove(3)
print(a1)
print(a2)
print(a3)
# 不可变集合

frozensetTest = frozenset([1,2,3,4,5])

print(frozensetTest)

keyDic = {frozensetTest:1, 33:2}

print(keyDic[frozensetTest])

# 不存在的时候赋值
if 'dd' in keyDic:
    print(keyDic['dd'])
else:
    print('屁都没有')
print(keyDic.get(10,'unknow'))
