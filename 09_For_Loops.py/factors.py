Question:
Write a program to print the factorial of N.
Factorial is the product of all positive integers less than or equal to N.
Note: The factorial of 0 is 1.

Input:
The input will be a single line containing a positive integer representing N.

Output:
The output should be a single line containing the factorial of the given number N.

Explanation:
For example, if the input is 4, the output should be 24.
(4 × 3 × 2 × 1 = 24)

Python Code:
a = int(input())
multiple = 1
for i in range(1, a + 1):
    multiple = multiple * i
print(multiple)

Testcase:
Case 1
Input:
4
Output:
24
