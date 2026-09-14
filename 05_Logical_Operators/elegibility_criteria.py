Write a program that reads the marks in Maths M, Physics P, and Chemistry C, and checks if any of the below conditions is satisfied.

- M > 60 and P > 60 and C > 60
- M + P + C >= 180

Input:
The first line of input contains an integer representing M.
The second line of input contains an integer representing P.
The third line of input contains an integer representing C.

Output:
True or False depending on whether any condition is satisfied.



m=int(input())
p=int(input())
c=int(input())
print((m>=70 and p>=60 and c>=60)or (m+p+c>=180))
