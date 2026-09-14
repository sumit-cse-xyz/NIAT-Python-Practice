Write a program that reads a four-digit number and checks if the first two digits of the number is 19 and the last two digits of the number is between 30 and 60.

Input:
The input will be a single line containing a four-digit integer.

Output:
The output should be a single line containing a boolean.
True should be printed if the first two digits of the number is 19 and the last two digits of the number is between 30 and 60, otherwise False should be printed.


a=input()
f2=int(a[:2])
l2=int(a[2:])
print(f2==19 and 30<l2<60)
