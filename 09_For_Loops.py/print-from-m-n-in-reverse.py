Question:
Write a program that reads two numbers M and N and prints the numbers from N to M in reverse order.

Input:
The first line of input will contain an integer representing M.
The second line of input will contain an integer representing N.

Output:
The output should contain all the integers from N to M, each on a new line.

Explanation:
For example, if M = 2 and N = 5:
Numbers from N to M in reverse are 5, 4, 3, 2.

Python Code:
a = int(input())
b = int(input())
for i in range(a,b+1):
    print(b-i+a)
Testcase:
Case 1
Input:
2
5
Output:
5
4
3
2

Case 2
Input:
3
7
Output:
7
6
5
4
3
