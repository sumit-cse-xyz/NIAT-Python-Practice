Write a program that reads an age A and guardian status S, and checks if the age A is between 12 and 60 or if the guardian status S is equal to yes.

Note:
The guardian status will be either yes or no.

Input:
The first line of input contains an integer representing the age.
The second line of input contains a string representing the guardian status.

Output:
True or False depending on whether any condition is satisfied.


a=int(input())
b=input()
print(12<a<60 or b=="yes" )
