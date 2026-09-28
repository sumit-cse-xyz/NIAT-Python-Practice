Question:
Write a program that reads two numbers M and N and prints the sum of squares of numbers from M to N.

Input:
The first line of input will contain an integer representing M.
The second line of input will contain an integer representing N.

Output:
The output should be a single line containing an integer that is the sum of squares of numbers from M to N.

Explanation:
For example, if the given numbers are M = 2 and N = 4:
The numbers from 2 to 4 are 2, 3, and 4.
The squares are 4, 9, and 16.
The sum of these squares is 29 (4 + 9 + 16 = 29).

Python Code:
a = int(input())
b = int(input())
sum = 0
for i in range(a, b + 1):
    sum = sum + (i * i)
print(sum)

Testcase:
Case 1
Input:
2
4
Output:
29
