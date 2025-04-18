c=int(input("Enter the number of m1 columes "))
r=int(input("Enter the number of m1 rows "))
i=r
j=r
ia=0
ja=0
ra=[]
ra2=[]
while r>0:
    r=r-1
    if i>0:
       i=i-1
       if j>0:
          j=j-1
          ij=int(input("enter ij "))
          ra.append(ij)
i=c
j=c

while c>0:
    c=c-1
    if i>0:
       i=i-1
       if j>0:
          j=j-1
          ij=int(input("enter ij "))
          ra2.append(ij)
print(ra)
print(ra2)

c2=int(input("Enter the number of m2 columes "))
r2=int(input("Enter the number of m2 rows "))
i=r2
j=r2
ia=0
ja=0
ra3=[]
ra4=[]
while r2>0:
    r2=r2-1
    if i>0:
       i=i-1
       if j>0:
          j=j-1
          ij=int(input("enter ij "))
          ra3.append(ij)
i=c2
j=c2

while c2>0:
    c2=c2-1
    if i>0:
       i=i-1
       if j>0:
          j=j-1
          ij=int(input("enter ij "))
          ra4.append(ij)
print(ra3)
print(ra4)

print("\nMatrix 1 is:- \n")
print(ra)
print(ra2)

print("\nMatrix 2 is:- \n")
print(ra3)
print(ra4)