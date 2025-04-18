def accm(M):
    print("Eneter the number of rows and colombs\n")
    r=int(input())
    c=int(input())
    for i in range (r):
        A=[]
        for j in range (c):
            a=int(input())
            A.append(a)
        M.append(A)

def dism(M,r,c):
   print("Matrix (%d,%d) : "%(r,c))
   for i in range(r) :
      print("\t\t",end=' ')
      for j in range(c):
          print("%3d"%M[i][j],end=' ')
      print("")

def addition_matrix(M1,M2,M3,r,c) :
    for i in range(r) :
        A = []        
        for j in range(c): 
           A.append(M1[i][j] + M2[i][j])
        M3.append(A)

def main():
    while True:
        print("\nenter 1 to accept and 0 to display or nathing")    
        y=int(input("\n1 or or 2 or 3 or 0 to end"))
        if y==1:
            M1=[]
            M2=[]  
            accm(M1)
            r1 = len(M1)
            c1 = len(M1[0])
            accm(M2)
            r2 = len(M2)
            c2 = len(M2[0])
        elif y==2:
            dism(M1,r1,c1)
            dism(M2,r2,c2)
        elif y==3:
            M3=[]
            if(r1 == r2 and c1 == c2) :
               addition_matrix(M1,M2,M3,r1,c1)
               dism(M1,r1,c1)
               print("\tAddition  ")
               dism(M2,r2,c2)
               dism(M3,r1,c1)
            else :
               print("Addition not possible (order not same)")
        elif y==0:
            break

main()
quit()