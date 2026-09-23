Question:
Write a program that reads two numbers M and N and prints a Rectangle of M rows and N columns using stars.

Input:
The first line of input contains an integer representing M.
The second line of input contains an integer representing N.

Output:
The output should be M rows and N columns containing stars (*) as a Rectangle shown in the sample output.

Python Code:
a = int(input())
x = int(input())
count = 0
while count < a:
    print('*' * x)
    count = count + 1

example:
Input:
4
5
Output:
*****
*****
*****
*****
