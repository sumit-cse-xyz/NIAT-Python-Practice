Question:
Given two numbers M and N, write a program to find the count of numbers from M to N that are divisible by 6.  
Print "No Numbers Found" if the count of numbers from M to N that are divisible by 6 is 0.  
Otherwise, print the numbers from M to N that are divisible by 6 separated by a space.

Input:
The first line of input contains an integer representing M.  
The second line of input contains an integer representing N.

Output:
Print all numbers between M and N that are divisible by 6 separated by a space.  
If none are divisible, print "No Numbers Found".

Explanation:
For example, if M = 6 and N = 23:  
Numbers divisible by 6 are 6, 12, 18.  
So, the output should be "6 12 18".

Python Code:
a=int(input())
b=int(input())
result=""
count=0
for i in range(a,b+1):
        if i%6==0:
            count=count+1
            result=result+str(i)+ " "
if count==0:
    print("No Numbers Found")
else:
    print(result)



Testcase:
Case 1  
Input:  
6  
23  
Output:  
6 12 18

Case 2  
Input:  
8  
10  
Output:  
No Numbers Found
