def accept_matrix(M) :
    print("\nEnter the order of the Matrix (row,col) : ")
    r = int(input("\trow = "))
    c = int(input("\tcol = "))
    print("Enter the elements of the Matrix : \n")
    for i in range(r) :
       A = []
       for j in range (c) :
          A.append(int(input()))
       M.append(A)
    print("\nMatrix accepted successfully\n")

def display_matrix(M,r,c): 
   print("Matrix (%d,%d) : "%(r,c))
   for i in range(r) :
      print("\t\t",end=' ')
      for j in range(c):
          print("%3d"%M[i][j],end=' ')
      print("")	

def change_row(M,r,c):
    for i in range(r):
        t=M[0][i]
        M[0][i]=M[r-1][i]
        M[r-1][i]=t

 
    for i in range(r):
        for j in range(c):
            print(M[i][j], end=" ")
        print("\t")
    
def find_transpose_matrix(M,r,c,T) :
    for i in range(c):
        A = []
        for j in range(r):
           A.append(M[j][i])
        T.append(A)

    for i in range(r):
        t2=T[0][i]
        T[0][i]=T[r-1][i]
        T[r-1][i]=t2
    
    for i in range(r):
        for j in range(c):
            print(T[i][j], end=" ")
        print("\t")

def change_row_2(M,r,c):
    for i in range(r):
        t2=M[0][i]
        M[0][i]=M[r-1][i]
        M[r-1][i]=t2
    
    for i in range(r):
        for j in range(c):
            print(M[i][j], end=" ")
        print("\t")

def change_sign(M1,M2,M3,r1,c1,c2) :
      for i in range(r1) :
        A = []
        for j in range(c2) : 
            sum = 0
            for k in range(c1) :
                sum = sum + (M1[i][k] * M2[k][j])
            A.append(sum)
        M3.append(A)
    




def main():   
   while True :
       print("\t\t\t1: Accept Matrix");
       print("\t\t\t2: Display Matrix");
       print("\t\t\t3: Addition of Matrices");
       print("\t\t\t4: Substraction of Matrices");
       print("\t\t\t5: Multiplication of Matrices");
       print("\t\t\t6: Transpose Matrix");
       print("\t\t\t7: Exit");

       ch = int(input("Enter your choice : "))
       M3 = []       
       if (ch == 7):
           print ("End of Program")
           break
       elif (ch==1):
           M1 = []
           M2 = []
           print("Input First Matrix ")
           accept_matrix(M1)
           r1 = len(M1)
           c1 = len(M1[0])
           print("Input Second Matrix ")
           accept_matrix(M2)
           r2 = len(M2)
           c2 = len(M2[0])
           
       elif (ch==2):
           print("\tFirst ",end=' ')
           display_matrix(M1,r1,c1)
           print("\tSecond ",end =' ')
           display_matrix(M2,r2,c2)
          
       elif (ch==6):
           print("\tFirst ",end=' ')
           display_matrix(M1,r1,c1)
           find_transpose_matrix(M1,r1,c1,M3);
           print("\tTranspose  ",end=' ');
           display_matrix(M3,c1,r1)
          
           M3 = []
           
       elif (ch==8):
           print("\tFirst :\n",end='')
           change_row(M1,r1,c1)
           

       elif (ch==9):
           change_row_2(M1,r1,c1);
          
         
       elif (ch==0):
        if(c1 == r2) :
               change_sign(M1,M2,M3,r1,c1,c2)
               print("\tSign change")
               display_matrix(M3,r1,c2)
        else :
               print("Sign change not possible ")
           
          
       else :
           print ("Wrong choice entered !! Try again")

main()
quit()