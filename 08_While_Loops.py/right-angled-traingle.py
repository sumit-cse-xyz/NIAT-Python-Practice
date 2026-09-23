Question:
Write a program that reads a number N and prints a Right Angled Triangle of N rows using stars (*).

Input:
The input will be a single line containing an integer representing N.

Output:
The output should be N rows containing stars forming a Right Angled Triangle.

Python Code:
a = int(input())
cont = 0
x = 0
while cont < a:
    x = x + 1
    print('*' * x)
    cont = cont + 1

example:
Input:
3
Output:
*
**
***
