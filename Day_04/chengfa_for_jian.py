for i in range(1,10):
    for j in range(i):
        j += 1
        print('%d*%d=%d'%(i,j,i*j),end="\t")
    print()