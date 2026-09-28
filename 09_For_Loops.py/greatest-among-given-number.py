Question:
Given a number N, write a program that reads N inputs and prints the greatest number among the given inputs.

Input:
The first line of input contains an integer representing N.
The next N lines of input contain integers.

Output:
The output should be a single line containing an integer that is the greatest among the given numbers.

Explanation:
For example, if the given number is N = 5 and the inputs are:
8
11
9
6
96
The output should be:
96

Python Code:
a = int(input())
b = int(input())
for i in range(a - 1):
    counter = int(input())
    if counter > b:
        b = counter
print(b)

Testcase:
Case 1
Input:
5
8
11
9
6
96
Output:
96

Case 2
Input:
3
10
25
7
Output:
25
