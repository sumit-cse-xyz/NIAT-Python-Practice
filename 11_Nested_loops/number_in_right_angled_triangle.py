#Question:- Given a number N write a program to print a Right Angled Triangle of N rows using numbers.
code:
a=int(input())
result=""
for j in range(1,a+1):
    y=""
    result=result+str(j)+" "
    for x in range(1,j):
          y=y+str(x)+" "
    print(result+y)
    
        
