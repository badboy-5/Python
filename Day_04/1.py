num1 = int(input("Num1:"))
num2 = int(input("Num2:"))
num3 = int(input("Num3:"))

if num1 > num2:
    if num1 > num3:
        print("最大的数是：%d"%num1)
    else:
        print("最大的数是：%d"%num3)
else:
    if num2 > num3:
        print("最大的数是：%d"%num2)
    else:
        print("最大的数是：%d"%num3)

