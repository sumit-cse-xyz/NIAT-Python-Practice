Question:
Write a program to check whether a given number is a Perfect Number or not.

Input:
The input will be a single integer representing N.

Output:
The output should be a single line containing either "Perfect Number" or "Not a Perfect Number".

Explanation:
A Perfect Number is a number that is equal to the sum of its factors (excluding itself).
For example, if N = 6:
Factors of 6 are 1, 2, and 3.
Sum of factors = 1 + 2 + 3 = 6, which is equal to the number itself.
So, the output should be "Perfect Number".

Python Code:
a = int(input())
result = 0
for i in range(1, a):
    if a % i == 0:
        result = result + i
if result == a:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

Testcase:
Case
