import json

def writeJson(file, data):
    data_str = json.dumps(data)
    with open(file, 'w') as w:
        w.write(data_str)

def readJson(file):
    with open(file,'r') as r:
        print(r.read())
    
class myJson:
    def __init__(self, fileName, data) -> None:
        self.fileName = fileName
        self.thisData = data

    def writeJson(self):
        data_str = json.dumps(self.thisData)
        with open(self.fileName, 'w',encoding='utf-8') as w:
            w.write(data_str)

    def readJson(self):
        with open(self.fileName, 'r',encoding='utf-8') as r:
            print(r.read().encode('utf-8').decode('utf-8'))


    #


