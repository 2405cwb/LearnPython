# author: cwb
# date: 2025/2/17
import json

class User:
    def __init__(self, userName, userPassword):
        self.userName = userName
        self.userPassword = userPassword

    def to_dict(self):
        return {
            'userName': self.userName,
            'userPassword': self.userPassword
        }

    def save_to_json(self, file_name):
        user_data = self.to_dict()
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(user_data, f, ensure_ascii=False, indent=4)


    @staticmethod
    def register(userName, userPassword, file_name='users.json'):
        new_user = User(userName, userPassword)
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                users = json.load(f)
        except FileNotFoundError:
            users = []

        for user in users:
            if user['userName'] == userName:
                print("用户名已存在，请选择其他用户名。")
                return False

        users.append(new_user.to_dict())
        
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(users, f, ensure_ascii=False, indent=4)
        return new_user

    @staticmethod
    def login(userName, userPassword, file_name='users.json'):
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                users = json.load(f)
        except FileNotFoundError:
            print("用户数据文件不存在，请先注册。")
            return False

        for user in users:
            if user['userName'] == userName and user['userPassword'] == userPassword:
                curUser = User(userName,userPassword)
                return curUser

        print("用户名或密码错误。")
        return False



# class User:
#     def __init__(self,userName,userPassword):
#         self.userName = userName
#         self.userPassword = userPassword
#         #查询本地是否存在
#         with open('users.json','r',encoding='utf-8') as r:
#             allUserData = r.read()
#             json.loads(r)


