death_age = 80  #定义一个变量为80

name = input("your name:")  #输入用户姓名
age = input("your age:")  #输入用户年龄

print(type(age))

print("Your name:",name)  #打印出用户姓名

print("You can still live for:",death_age-int(age),"year")  #不使用int将会报错

# 将三个字符串拼接
print("You can still live for:"+ str(death_age-int(age)) +"year")  #不使用str将会报错