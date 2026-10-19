#Given a number N, write a program to print an Inverted Right Angled Traingle of N rows using numbers starting from 1.
Code:
a=int(input())
for i in range(1,a+1):
        b=a+1
        b=b-i
        x=1
        while b>0:
          print(x,end=" ")
          x=x+1
          b=b-1
        print()
        
