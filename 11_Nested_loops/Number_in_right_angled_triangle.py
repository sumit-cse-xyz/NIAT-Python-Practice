#Given a number N write a program to print a RIGHT ANGLED TRIANGLE of N rows using numbers staring from 1.
code:
a=int(input())
result=""
for i in range(1,a+1):
    result=result+str(i)+" "
    print(result)
