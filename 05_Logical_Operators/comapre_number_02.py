Write a program that reads a three-digit number and checks if any of the below conditions is satisfied.

• Each digit of the given number is greater than 7.
• The product of any two digits is always less than or equal to 30.

Input:
The input will be a single line containing a three-digit integer.

Output:
The output should be a single line containing a boolean.
True should be printed if each digit of the given number is greater than 7 or if the product of any two digits is less than or equal to 30.


a=(input())
first=int(a[0])
second=int(a[1])
third=int(a[2])
p1= (first) * (second)
p2= (first) * (third)
p3= (third) * (second)
print((first>7 and second>7 and third>7) or (p1<=30 and p2<=30 and p3<=30))
