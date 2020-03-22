age = 25

# flag = True
#
# while flag:
#     user_inpu_age = int(input("Enter Age:"))
#     if user_inpu_age == age:
#         print("You Are Right!")
#         flag = False
#     elif user_inpu_age > age:
#         print("So Bigger!")
#     else:
#         print("So Smaller!")
# print("Over！")

while True:
    user_inpu_age = int(input("Enter Age:"))
    if user_inpu_age == age:
        print("You Are Right!")
        break
    elif user_inpu_age > age:
        print("So Bigger!")
    else:
        print("So Smaller!")
print("Over！")