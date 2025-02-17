import pickle
def foo():
    print('ok')
methodData = pickle.dumps(foo)

with open('pickle.txt','wb') as w:
    w.write(methodData)


with open('pickle.txt','rb') as w:
    data = w.read()
    readData = pickle.loads(data)
    readData()
    print(readData)