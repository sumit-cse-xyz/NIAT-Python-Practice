Question:
Given two numbers X and N, write a program to print the sum of N terms in the given series.

Series:
(X)^2, (XX)^2, (XXX)^2, ... N terms

Input:
The input will be two integers separated by a newline representing X and N.

Output:
The output should be a single integer representing the sum of N terms in the given series.

Explanation:
For example, if X = 4 and N = 3:
Series terms are 4, 44, 444
Sum = (4)^2 + (44)^2 + (444)^2 = 16 + 1936 + 197136 = 199088

Python Code:
a = int(input())
b = int(input())
result = 0
for i in range(1, b + 1):
    i = i * str(a)
    result = result + (int(i) ** 2)
print(result)

Testcase:
Case
