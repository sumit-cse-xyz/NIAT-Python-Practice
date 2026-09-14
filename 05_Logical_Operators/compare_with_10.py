Write a program that reads two numbers A and B, and checks if any of the following conditions are satisfied:

- The sum of A and B is less than 10.
- The difference between A and B is less than 10.
- A is between 5 and 30.



a=int(input())
b=int(input())
print((a<10 and b<10) or (a-b < 10) or (5<a<30))
