Question:
Given a number N, write a program to print the sum of the Kth power of all the digits in the given number.
K indicates the number of digits of the number N.

Input:
The input will be a single line containing an integer representing N.

Output:
The output should be a single line containing an integer that is the sum of the Kth power of all the digits of the number N.

Explanation:
For example, if N = 17:
Number of digits (K) = 2
Sum = 1^2 + 7^2 =50

Python Code:
a = input()
b = len(a)
result = 0
for i in a:
    result = result + (int(i) ** b)
print(result)

Testcase:
Case 1
Input:
24753
Output:
71235

Case 2
Input:
17
Output:
50
