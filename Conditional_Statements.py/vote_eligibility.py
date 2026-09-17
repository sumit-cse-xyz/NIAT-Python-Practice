Question:
Write a program that reads the age of a person and checks if the age of the person is greater than or equal to 18 for eligibility to vote.
Print Eligible if the age of the person is greater than or equal to 18, otherwise print Not Eligible.

Input:
The input will be a single line containing an integer.

Output:
The output should be a single line containing a string.
Eligible should be printed if the age of the person is greater than or equal to 18, otherwise Not Eligible should be printed.



a=int(input())
if a>=18:
 print("Eligible")
else:
     print("Not Eligible")
