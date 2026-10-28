#Given two numbers M and N, write a program to print the Least common multiple(L.C.M) of the numbers M and N.
CODE//
a=int(input())
b=int(input())
if b>a:
    larger=b
else:
    larger=a 
for i in range(1,larger+1):
    if (larger*i)%a==0 and (larger*i)%b==0:
        print(larger*i)
        break
