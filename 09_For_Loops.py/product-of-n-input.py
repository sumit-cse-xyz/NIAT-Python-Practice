Question:
Given an integer N, write a program which reads N inputs and prints the product of the given input integers.

Input:
The first line of input will contain a positive integer, N.
The next N lines will contain the integers, each in a line.

Output:
The output should be a single line containing an integer that is the product of the given inputs.

Explanation:
For example, if the given number is N = 3,
The 3 inputs are 2, 3, and 7.
The product of the given inputs is 42. (2 * 3 * 7 = 42)

Python Code:
a = int(input())
cont = 1
for i in range(a):
    cont = cont * int(input())
print(cont)

Testcase:
Case 1
Input:
3
2
3
7
Output:
42
