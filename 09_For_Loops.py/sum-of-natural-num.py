Question:
Write a program that reads a number N and prints the sum of Natural Numbers from 1 to N.

Note:
Use the For loop to iterate over the range of numbers.

Input:
The input will be a single line containing an integer representing N.

Output:
The output should be a single line containing an integer that is the sum of Natural Numbers from 1 to N.

Example:
Input:
6

Output:
21


a = int(input())
cont = 0
for i in range(1, a + 1):
    cont = cont + i
print(cont)
