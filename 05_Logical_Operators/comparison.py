COMPARE NUMBERS - 2

Write a program that reads two numbers A and B, and checks if one of the given numbers is a negative number and the sum of the given numbers is greater than 7.

Input:
The first line of input contains an integer representing A.
The second line of input contains an integer representing B.

Output:
The output should be a single line containing a boolean.
True should be printed if one of the given numbers is a negative number and the sum of the numbers is greater than 7, otherwise False should be printed.


a=int(input())
b=int(input())
print((a<0 or b<0) and (int(a)+int(b)>7))
