Question:
Write a program that reads a number M and prints a Square of M rows and M columns using numbers.

Note:
Use For loop.

Input:
The input will be a single line containing an integer representing M.

Output:
The output should be M rows and M columns printed using numbers.

Example:
If M = 4, the output should be:
1111
2222
3333
4444

Python Code:
a = int(input())
for i in range(1, int(a) + 1):
    print(str(i) * int(a))

Testcase:
Case 1
Input:
4
Output:
1111
2222
3333
4444
