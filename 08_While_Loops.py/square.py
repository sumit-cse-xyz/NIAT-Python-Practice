Question:
Write a program that reads a number N and prints a Square of N rows and N columns using numbers starting from 1.

Input:
The input will be a single line containing an integer representing N.

Output:
The output should be N rows containing numbers as a Square shown in the sample output.

example:
Input:
4
Output:
1111
2222
3333
4444


Python Code:
a = int(input())
count = 0
b = 1
while count < a:
    print(str(b) * a)
    count = count + 1
    b = b + 1

