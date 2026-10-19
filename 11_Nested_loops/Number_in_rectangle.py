#Given two number M and N, write a program to print a Rectangle of M rows and N columns using numbers starting from 1.
Code:
a=int(input())
b=int(input())
x=1 
for i in range(1,a+1):
    for j in range(1,b+1):
        print(x,end=" ")
        x+=1 
    print()
