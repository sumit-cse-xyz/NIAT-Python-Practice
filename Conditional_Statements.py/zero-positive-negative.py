Question:
Write a program that reads a number and checks if the given number is zero, positive or negative.
Print Zero if the given number is equal to 0.
Print Positive if the given number is greater than 0.
Print Negative if the given number is less than 0.

Input:
The input will be a single line containing an integer.

Output:
The output should be a single line containing a string.
Zero should be printed if the given number is equal to 0.
Positive should be printed if the given number is greater than 0.
Negative should be printed if the given number is less than 0.


a=int(input())
if a>0:
    print("Positive")
elif a<0:
    print("Negative")
else :
    print("Zero")
