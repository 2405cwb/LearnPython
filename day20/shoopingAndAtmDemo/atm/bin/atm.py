from user import User

current_user = None
 
def Log_Mehod(choice, userName, userPassword):
    if choice == '1':
        userName = input("请输入用户名: ")
        userPassword = input("请输入密码: ")
        login_result = User.login(userName, userPassword)
        print(type(login_result))
        if isinstance(login_result,User):
            print("登录成功！")
        else:
            print("登录失败！")
    elif choice == '2':
        userName = input("请输入用户名: ")
        userPassword = input("请输入密码: ")
        registration_result = User.register(userName, userPassword)
        if isinstance(registration_result, User):
            current_user = registration_result
            print("注册成功！")
        else:
            print("注册失败！")
    else:
        print("无效的选择，请输入1或2。")
