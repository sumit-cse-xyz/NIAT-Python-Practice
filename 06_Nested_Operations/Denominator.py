Question:
Write a program that reads an amount A and prints the minimum number of 5 and 1 rupee notes required for the given amount.

Input:
The input will be a single line containing an integer representing the amount A.

Output:
The first line of output should be a string containing the required number of 5 rupee notes as shown in the sample output.
The second line of output should be a string containing the required number of 1 rupee notes as shown in the sample output.

example
  input=16
  output=  5:3
           1:1



a=int(input())
b= int(a/5)
c=int(a- (5*b))
print("5"+":"+str(b))
print("1"+":"+str(c))
