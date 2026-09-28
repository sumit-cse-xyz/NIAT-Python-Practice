Question:
Write a program that reads two numbers M and N and prints the count of numbers between M and N (inclusive) that are divisible by both 2 and 3.

Input:
The first line of input will contain an integer representing M.
The second line of input will contain an integer representing N.

Output:
The output should be a single line containing the count of numbers between M and N that are divisible by both 2 and 3.

Explanation:
For example, if M = 1 and N = 12:
Numbers from 1 to 12 are 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, and 12.
The numbers divisible by both 2 and 3 are 6 and 12.
The count is 2.

Python Code:
a = int(input())
b = int(input())
result = 0
for i in range(a, b + 1):
    if i % 2 == 0 and i % 3 == 0:
        result += 1
print(result)

Testcase:
Case 1
Input:
1
12
Output:
2

Case 2
Input:
21
30
Output:
2
