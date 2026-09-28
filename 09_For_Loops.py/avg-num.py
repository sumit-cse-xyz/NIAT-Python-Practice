Question:
Write a program that reads a number N and prints the average of numbers from 1 to N.

Note:
Use the For loop to iterate over the range of numbers.

Input:
The input will be a single line containing an integer representing N.

Output:
The output should be a single line containing a float that is the average of numbers from 1 to N.

Example:
If N = 3, the average of numbers from 1 to 3 is:
Average = (1 + 2 + 3) / 3 = 2.0

Python Code:
a = int(input())
cont = 0
for i in range(1, a + 1):
    cont = cont + i
print(cont / a)

Testcase:
Case 1
Input:
8
Output:
4.5
