num1 = 1

while num1 <= 9:
    num2 = 1
    while num2 <= num1:
        print(num2,end="*")
        print(num1, end="=")
        print(num1*num2,end="\t")
        # print('%d*%d=%d'%(num2,num1,num1*num2) ,end="\t")
        num2 += 1
    num1 += 1
    print()