Question:
Print Can team up if one of the scores is greater than 300 and the sum of the scores is less than 500, otherwise print Cannot team up.

Input:
The first line of input contains an integer representing the score A.
The second line of input contains an integer representing the score B.

Output:
The output should be a single line containing a string.
Can team up should be printed if one of the scores is greater than 300 and the sum of the scores is less than 500, otherwise Cannot team up should be printed.



a=int(input())
b=int(input())
if (a>300 or b>300) and (a+b<500):
    print("Can team up")
else:
 print("Cannot team up")
