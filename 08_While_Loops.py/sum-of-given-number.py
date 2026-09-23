Question:
Given an integer N, write a program which reads N inputs and prints the sum of the given input integers.

Input:
The first line of input will contain a positive integer, N.
The next N lines will contain the integers, each in a line.

Output:
The output should be the sum of the given input integers.

Explanation:
For example, if the given N is 3, then read the inputs in the next 3 lines and print the sum of the three input integers.
If the given input integers in the next three lines are 8, 11, and 25, the output should be 44.

Python Code:
a = int(input())
counter = 0
sum = 0
while counter < a:
    num = int(input())
    counter = counter + 1
    sum = sum + num
print(sum)

Testcase:
Case 1
Input:
3
8
11
25
Output:
44
