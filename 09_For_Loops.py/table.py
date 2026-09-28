Question:
Write a program to print the multiplication table of the given number (N) up to ten multiples in the format "N x i = M".

Input:
The first line of input will contain an integer.

Output:
The output should be ten lines containing the multiples in the given format.

Explanation:
For example, if the given number is 3:
Your code should print the multiplication table like:
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30

Python Code:
a=int(input())

for i in range(1,11):
    result=str(a) + " x "+ str(i) +" = "
    multiply=i*a  
    print(result+str(multiply))


Testcase:
Case 1
Input:
3
Output:
3 x 1 = 3
3 x 2 = 6
3 x
