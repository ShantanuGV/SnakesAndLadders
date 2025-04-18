SEB=[]
Badminton=[]
Badminton1=[]
Cricket=[]
Cricket1=[]
Football=[]
Football1=[]
n=0

def remove_dup(d):
    lst=[]
    for i in d:
        if i not in lst:
            lst.append(i)
    return(lst)

def se_b():
    global n
    n=int(input("Enter the number of students : "))
    for i in range(1,n+1):
        print("Enter the names of the students ",i,":")
        s=(input())
        SEB.append(s)
    print("List of students:" + str(SEB))

def se_badminton():
    global n
    n=int(input("Enter the number of students playing Badminton : "))
    for i in range(1,n+1):
        print("Enter the name of the student ",i,":")
        s=(input())
        Badminton.append(s)
    print("Students playing Badminton are : " + str(Badminton))
    Badminton1=remove_dup(Badminton)
    print("Updated list of students playing Badminton:" + str(Badminton1))

def se_cricket():
    global n
    n=int(input("Enter the number of students playing Cricket : "))
    for i in range(1,n+1):
        print("Enter the name of the student ",i,":")
        s=(input())
        Cricket.append(s)
    print("Students playing Cricket are : " + str(Cricket))
    Cricket1=remove_dup(Cricket)
    print("Updated list of students playing Cricket:" + str(Cricket1))

def se_football():
    global n
    n=int(input("Enter the number of students playing Football : "))
    for i in range(1,n+1):
        print("Enter the name of the student ",i,":")
        s=(input())
        Football.append(s)
    print("Students playing Football are : " + str(Football))
    Football1=remove_dup(Football)
    print("Updated list of students playing Football:" + str(Football1))

def Union(lst1,lst2):
    lst3=lst1.copy()
    for val in lst2:
        if val not in lst3:
            lst3.append(val)
            print("Union of students playing Badminton and Cricket are:" +
        str(lst3))
    return lst3

def Intersection(lsta,lstb):
    lstc=[val for val in lsta if val in lstb]
    print("Intersection of students playing Badminton and Cricket are:" +
    str(lstc))
    return lstc

def sub(lst2,lst1):
    lst3=[]
    for val in lst2:
        if val not in lst1:
            lst3.append(val)
            print(str(lst3))
    return lst3

def subtract(lst1,lst2):
    lst3=[]
    for val in lst1:
        if val not in lst2:
            lst3.append(val)
    print("s1-s2=" + str(lst3))
    return lst3

def symmetric(lst1,lst2):
    lst3=[]
    lst4=subtract(lst1,lst2)
    print("Difference between Badminton and Cricket (B-C) is :" + str(lst4))
    lst5=sub(lst2,lst1)
    print("Difference between Cricket and Badminton (C-B) is :" + str(lst5))
    lst3=Union(lst4,lst5)
    print("symmetric difference is :",str(lst3))
    return lst3

se_badminton()
se_cricket()
se_football()
Union(Badminton,Cricket)
Intersection(Badminton,Cricket)
sub(Badminton,Cricket)
subtract(Cricket,Badminton)
symmetric(Badminton,Cricket)
flag=1
while flag==1:
    print("\n ******MENU*******\n")
    print("1. List of students who play both Cricket and Badminton:")
    print("2. List of students who play either Cricket or Badminton but not both:")
    print("3. List of students who play neither Cricket nor Badminton:")
    print("4. List of students who play Cricket and Football but not Badminton:")
    print("5. Exit:")
    ch=int(input("Enter the choice from 1 to 5:"))

    if ch==1:
        print("List of students who play both Cricket and Badminton:",Intersection(Badminton,Cricket))
        a=input("\n\n Continue(y/n):")
        if a=="y"or"Y":
            flag=1
        else:
            flag=0
        print("Thank you!")

    elif ch==2:
        print("List of students who play either Cricket or Badminton but not both:",symmetric(Badminton,Cricket))
        a=input("\n\n Continue(y/n):")
        if a=="y"or"Y":
            flag=1
        else:
            flag=0
        print("Thank you!")

    elif ch==3:
        print("List of students who play neither Cricket nor Badminton:",remove_dup(Football))
        a=input("\n\n Continue(y/n):")
        if a=="y"or"Y":
            flag=1
        else:
            flag=0
        print("Thank you!")

    elif ch==4:
        lst3=Union(Cricket,Football)
        lst4=Badminton
        lst5=subtract(lst3,lst4)
        print("List of students who play Cricket and Football but not Badminton:",lst5)
        a=input("\n\n Continue(y/n):")
        if a=="y"or"Y":
            flag=1
        else:
            flag=0
        print("Thank you!")

    elif ch==5:
        flag=0
        print("Thank you for using the program!")


    else:
        print("Wrong Choice!!!")
        a=input("\n\n Continue(y/n):")
        if a=="y" or "Y":
            flag=1
        else:
            flag=0
        print("Thank You for using the program!")