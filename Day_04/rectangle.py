high = int(input("Please input high:"))
wide = int(input("Please input wide:"))
a = 1

while a <= high:
    b = 1
    while b <= wide:
        print("#",end="")
        b += 1
    print()
    a += 1