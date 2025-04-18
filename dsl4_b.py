#Write a Python program to store roll numbers of student array who attended training program in sorted order. 
#Write function for searching whether particular student attended training program or not, using Binary search
#and Fibonacci search

def accept_array(A):
    n = int(input("\n Enter the total no. of student : "))
    print("\n Input roll numbers in sorted order")
    for i in range(n):
        x = int(input("Enter the roll no of student %d : "%(i+1)))
        A.append(x)
    print("Student Info accepted successfully\n\n")
    return n
def display_array(A,n):
    if(n == 0) :
        print("\n No records in the database")
    else :
        print("Students Array : ",end=' ')
        for i in range(n) :
            print("%d "%A[i],end=' ')
            print("\n")
def Recursive_Binary_Search(A,s,l,X) :
    if(s <= l ) :
        mid = int((s + l) / 2)
    if(A[mid] == X) :
        return mid
    else :
        if(X < A[mid] ) :
            return Recursive_Binary_Search(A,s,mid-1,X)
        else :
            return Recursive_Binary_Search(A,mid+1,l,X)
    return -1
def Iterative_Binary_Search(A,n,X) :
    s = 0
    l = n-1
    while(s <= l ) :
        mid = int((s + l) / 2)
        if(A[mid] == X) :
            return mid
        else :
            if (X < A[mid] ) :
                l = mid-1
            else :
                s = mid+1
    return -1
def Fibonacci_Search(A,n,X) :
    f1 = 0
    f2 = 1
    f3 = f1 + f2
    offset = -1
    while (f3 < n) :
        f1 = f2
        f2 = f3
        f3 = f1 + f2
    while (f3 > 1) :
        i = min(offset+f1, n-1)
        if(A[i] == X) :
            return i
        else :
            if (X < A[i] ) :
                f3 = f1
                f2 = f2 - f1
                f1 = f3 - f2
            else :
                f3 = f2
                f2 = f1
                f1 = f3 - f2
                offset = i
        if(f2 == 1 and (offset+1) < n and A[offset + 1] == X) :
            return offset+1
    return -1
def Main() :
    A = []
    while True :
        print ("\t 1. Accept & Display Students info ")
        print ("\t 2. Recursive Binary Search")
        print ("\t 3. Iterative Binary Search")
        print ("\t 4. Fibonacci Search")
        print ("\t 5. Exit")
        ch = int(input("\n\n Enter your choice : "))
        if (ch == 5):
            print ("End of Program")
            quit()
        elif (ch==1):
            A = []
            n = accept_array(A)
            display_array(A,n)
        elif (ch==2):
            X = int(input("Enter the roll no. to be searched : "))
            flag = Recursive_Binary_Search(A,0,n-1,X)
            if(flag == -1) :
                print("\t Roll no. to be Searched not Found\n")
            else :
                print("\t \n \n Roll no. found at location %d"%(flag + 1))
        elif (ch==3):
            X = int(input("Enter the roll no. to be searched : "))
            flag = Iterative_Binary_Search(A,n,X)
            if(flag == -1) :
                print("\t Roll no. to be Searched not Found\n")
            else :
                print("\t \n \n Roll no. found at location %d"%(flag + 1))
        elif (ch==4):
            X = int(input("Enter the roll no. to be searched : "))
            flag = Fibonacci_Search(A,n,X)
            if(flag == -1) :
                print("\t Roll no. to be Searched not Found\n")
            else :
                print("\t \n \n Roll no. found at location %d"%(flag + 1))
        else :
            print ("Wrong choice")
Main()