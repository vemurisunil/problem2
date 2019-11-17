num = int(input("number"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end='')
    z=i
    for j in range(1,z):
        print(z-j,end='')
    print()