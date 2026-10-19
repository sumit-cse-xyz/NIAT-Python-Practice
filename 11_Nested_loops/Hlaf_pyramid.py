#Write a program to print the numbers in the given N number of rows in the following half pyramid pattern.
Code:
a=int(input())
x=1
for i in range(1,a+1):
    while i>0:
        print(x,end=" ")
        x=x+1
        i=i-1
    print()
    
