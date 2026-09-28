Question:
Write a program that reads a number N and prints a Right Angled Triangle of N rows using stars (*) and pluses (+).

Input:
The input will be a single line containing an integer N.

Output:
The output should be N rows — the first N−1 rows contain stars (*) and the Nth row contains pluses (+).

Example:
If N = 4, the output should be:
*
**
***
++++

Python Code:
a = int(input())
for i in range(1, a + 1):
    if i < a:
        print("*" * i)
    else:
        print("+" * i)

Testcase:
Case 1
Input:
4
Output:
*
**
***
++++
