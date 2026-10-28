#Queston:- Given two numbers M and N, write a program to print the Greatest common Divisor (G.C.D) of the numbers M to N.
CODE//
a=int(input())
b=int(input())
if a!=b:
  for i in range(2,a+1):
    i=a-i
    if a%i==0 and b%i==0:
        print(i)
        break
  else:
     print("1")
else:
    print(a)
