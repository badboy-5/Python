num1 = 1

for num1 in range(1,10):
    # print(num1,end="*")
    num2 = 1
    for num2 in range(1,num1+1):
        print(num2,end="*")
        print(num1, end="=")
        print(num1*num2,end="\t")
        # print(str(num2) + "*" + str(num1) + "=" + str(num1 * num2), end="\t")
    print()