Question:
Write a program that reads the three angles A, B, and C of a Triangle and checks if the sum of the three angles of the Triangle is equal to 180.
Print the Triangle as given below if the sum of the three angles of the Triangle is equal to 180.
Otherwise, print Not a Valid Triangle.

Input:
The first line of input contains an integer representing angle A.
The second line of input contains an integer representing angle B.
The third line of input contains an integer representing angle C.

Output:
The output should be a single line or multiple lines containing a string.
Print the Triangle pattern as shown below if the sum of the three angles is equal to 180.
Otherwise, print Not a Valid Triangle.


a=int(input())
b=int(input())
c=int(input())
sum=a+b+c 
if (a+b+c==180):
    print("*")
    print("**")
    print("***")
else:
    print("Not a Valid Triangle")
