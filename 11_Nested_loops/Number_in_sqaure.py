#Given a number N wite a program to print a Square of N rows using numbers starting form 1.
code:
a=int(input())
result=""
for i in range(1,a+1):
    result=result+str(i)+" "
for i in range(1,a+1):
    print(result)
