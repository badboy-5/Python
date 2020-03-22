Line = int(input("Please Input Line:"))

num = 1
while num <= Line:
    num2 = Line
    while num2 >= num:
        print("*",end=" ")
        num2 -= 1
    print()
    num += 1