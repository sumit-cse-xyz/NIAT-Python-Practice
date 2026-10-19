#Given a number N, wirte a program to print Armstrong numbera form 1 to N each on a new line.
Code:
a=int(input())
for i in range(1,a+1):
    b=len(str(i))
    result=0
    for j in str(i):
        result=result+int(int(j)**b)
    if result==i:
        print(i)
