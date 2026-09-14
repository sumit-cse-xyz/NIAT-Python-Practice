Write a program that reads two numbers A and B and checks if both the sum and the product of the given numbers have less than three digits.

Input:
The first line of input contains an integer representing A.
The second line of input contains an integer representing B.

Output:
The output should be a single line containing a boolean.
True should be printed if both the sum and the product of the given numbers have less than three digits, otherwise False should be printed.



a=int(input())
b=int(input())
sum=a+b 
product=a*b 
print(sum<100 and product<100)
