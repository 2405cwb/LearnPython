import copy
a = [[1, 2, 3], 22, 33]
b = a.copy()
b[0][1] = 3333
print(a)
print(b)


c = copy.deepcopy(a)
c[0][1] = 456421

print(a)
print(c)

