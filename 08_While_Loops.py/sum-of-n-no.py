Question:
Write a program that reads a number N and prints the sum of the first N natural numbers.

Input:
The input will be a single line containing an integer representing N.

Output:
The output should be a single line containing an integer that is the sum of the first N natural numbers.

Python Code:
a = int(input())
con = 0
b = 0
while con < a:
    con = con + 1
    b = b + con
print(b)

example:
Input: 6
Output: 21
