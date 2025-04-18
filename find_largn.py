n1=int(input("Enter number 1"))
n2=int(input("Enter number 2"))
n3=int(input("Enter number 3"))

print(n1,n2,n3,"\n")

if n1>n2:
    if n1>n3:
        print(n1,"is gratest")
    else:
        print(n3,"is gratest")
elif n2>n1:
    if n2>n3:
        print(n2,"is gratest")
    else:
        print(n3,"is gratest")
elif n3>n1:
    print(n3,"is gratest")
else:
    print(n1,n2,n3,"all are equle")     
