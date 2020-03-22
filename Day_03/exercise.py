#编写登录入口
# 输入用户名和密码
# 认证成功后显示欢迎信息
# 输错三次后锁定
# 再次打开代码，依旧是锁定状态
user_name_true = "jay"
user_password_true = "1234"

for i in range(3):
    file = open('lock.txt').readlines()
    user_name_input = input("请输入你的用户名：").strip()

    lock=[]
    for n in file:
        line = n.strip('\n')
        lock.append(line)
    if user_name_input in lock:
        print("The account！")
        break
    user_password_input = input("请输入你的密码：")
    if user_name_input != user_name_true or user_password_input != user_password_true:
            if i >= 2:
                print("The account！")
                break
            else:
                print("Try again！You have ",2-i, "chance!")
                i += 1
    else:
        print("Welcom!")
        break
