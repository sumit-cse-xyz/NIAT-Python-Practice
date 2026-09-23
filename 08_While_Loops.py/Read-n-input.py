Question:
Given an integer N, write a program which reads N inputs and prints them.

Input:
The first line of input will contain a positive integer, N.
The following N lines will contain an integer in each line.

Output:
The output should be N lines, containing an integer per line.
example: 
Input:
3
8
11
25
Output:
8
11
25


Explanation:
For example, if the given N is 3, then read the inputs in the next 3 lines and print them.
If the given input integers in the next three lines are 8, 11, and 25, the output should be:
8
11
25


Python Code:
a = int(input())
counter = 0
while counter < a:
    num = int(input())
    print(num)
    counter = counter + 1

