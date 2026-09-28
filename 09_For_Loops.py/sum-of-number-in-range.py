Question:
Given two integers M and N, write a program to print the sum of the numbers from M to N.

Input:
The first line of input will contain an integer.
The second line of input will contain an integer.

Output:
The output should be a single line containing the sum of the numbers from M to N.

Explanation:
For example, if the given numbers are 2 and 6, the output should be 20.
(2 + 3 + 4 + 5 + 6 = 20)

Python Code:
a = int(input())
b = int(input())
cont = 0
for i in range(a, b + 1):
    cont = cont + i
print(cont)

Testcase:
Case 1
Input:
2
6
Output:
20
