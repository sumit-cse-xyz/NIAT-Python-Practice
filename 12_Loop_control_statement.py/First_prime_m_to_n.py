#Question:- Given two numbers M and N . Write a program to print the first prime number from M to N. If no prime numbers are present from M to N print No prime numbers in the given range.
Code//
a=int(input())
b=int(input())
if a>1:
    for i in range(a,b+1):
        count=1
        for j in range(2,i):
          if i%j==0:
             count=0
        if count==1:
           print(i)
           break
    else:
        print("No prime numbers in the given range")
else:
    print("2")
