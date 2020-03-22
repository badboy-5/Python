user_name_true = "jay"
user_password_true = "1234"

for i in range(3):
    user_name_input = input("请输入你的用户名：").strip()
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