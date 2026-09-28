Question:
Write a program that reads two numbers M and N and prints the sum of all even numbers between M and N (inclusive).

Input:
The first line of input will contain an integer representing M.
The second line of input will contain an integer representing N.

Output:
The output should be a single line containing the sum of all even numbers between M and N.

Explanation:
For example, if the given numbers are M = 2 and N = 6:
The even numbers between 2 and 6 are 2, 4, and 6.
The sum of these even numbers is 12 (2 + 4 + 6 = 12).

Python Code:
a = int(input())
b = int(input())
sum = 0
for i in range(a, b + 1):
    if i % 2 == 0:
        sum = sum + i
print(sum)

Testcase:
Case 1
Input:
2
6
Output:
12
