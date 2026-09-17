Question:
Write a program that reads three numbers A, B, and C and prints the greatest among the three numbers.

Input:
The first line of input contains an integer representing A.
The second line of input contains an integer representing B.
The third line of input contains an integer representing C.

Output:
The output should be a single line containing an integer that is the greatest among the three numbers.

a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)
