n=(int(input("Entre the Tolat Numner of elements in list :- ")))
a=[]
i=0

while i<n :
    b=(int(input("Entre the elements in list :- ")))
    a.append(b)
    i=i+1

s=(int(input("Entre the elements in list to search by linear s* :- ")))

i=0

while i<n :
    print(a[i])
    if s==a[i]:
        print("Number",s,"has found on index location",i)
        break
    i=i+1
