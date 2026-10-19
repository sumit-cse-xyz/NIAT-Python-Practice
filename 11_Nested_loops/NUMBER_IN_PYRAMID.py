#Given two numbers S and N, write a program to print a Pyramid of N rows using numbera staring from S.
CODE:
a=int(input())
b=int(input())
for i in range(1,b+1):
     print(" "*(b-i),end="")
     for j in range(a,a+i):
         print(j,end=" ")
     print()
