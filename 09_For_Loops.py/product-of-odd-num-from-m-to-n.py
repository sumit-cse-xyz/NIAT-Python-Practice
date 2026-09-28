Question:
Write a program that reads two numbers M and N and prints the product of all odd numbers between M and N (inclusive).

Input:
The first line of input will contain an integer representing M.
The second line of input will contain an integer representing N.

Output:
The output should be a single line containing the product of all odd numbers between M and N.

Explanation:
For example, if the given numbers are M = 2 and N = 7:
Numbers from 2 to 7 are 2, 3, 4, 5, 6, and 7.
The odd numbers among them are 3, 5, and 7.
The product of these odd numbers is 105 (3 × 5 × 7 = 105).

Python Code:
a = int(input())
b = int(input())
product = 1
for i in range(a, b + 1):
    if i % 2 == 1:
        product = product * i
print(product)

Testcase:
Case 1
Input:
2
7
Output:
105
