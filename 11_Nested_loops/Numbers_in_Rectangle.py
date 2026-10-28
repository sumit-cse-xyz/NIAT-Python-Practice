#Given two number M and N, write a program to print a Rectangle of M rows and N column that containes numbers starting from K in decending order. K is the count of numbers that can be printed in M rows and N columns of a Rectangle.
code//
a=int(input())
b=int(input())
x=a*b
for i in range(1,a+1):
    for i in range(1,b+1):
        print(x,end=" ")
        x=x-1
    print()
