a=[2,1,3,6,7,9,8,32,65,4,1,6,8,65]
a2=[2,1,3,6,7,9,8,32,65,4,1,6,8,65]
b=0
i=0
j=0
t=0
n=len(a)
print("n is",n,"\n")
print(a2)
while i<n:
    t=t+1
    b=a2[i]
    j=1+i
    if j<n:
        print(a2)
        if b > a2[j]:
            c=a2[j]
            a2[j]=a2[i]
            a2[i]=c
            print(a2)

        print(i)

        print(a2[i])  
        h=i-1

    if h>=0:      
        if a2[h]>a2[i]:
            i=i-1
            print(".")
        else:
            i=i+1
    else:
        i=i+1        
            
print(a2)
print(t)