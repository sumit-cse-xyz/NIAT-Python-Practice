Question:
Write a program that reads a number N and prints all the factors of N.

Input:
The input will be a single integer representing N.

Output:
The output should contain all the factors of N, each on a new line.

Explanation:
For example, if N = 15:
Numbers that divide 15 completely are 1, 3, 5, and 15.
So the output should be:
1
3
5
15

Python Code:
a = int(input())
for i in range(1, a + 1):
    if a % i == 0:
        print(i)

Testcase:
Case 1
Input:
6
Output:
1
2
3
6

Case 2
Input:
15
Output:
1
3
5
15
