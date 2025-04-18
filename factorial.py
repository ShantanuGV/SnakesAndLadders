print("**********Factorial Finder**********\n")
n=int(input("Enter the number : "))
n2=n
print("\nYour entered number is",n,"!")
a=1
if n>=0:
 while n>0:
    a=a*n;
    n=n-1;
    if n==0:
        break;
 print("The Factorial of",n2,"is",a)

else:
   while n<0:
    a=a*n;
    n=n+1;
    if n==0:
        break;
   print("The Factorial of",n2,"is",a)