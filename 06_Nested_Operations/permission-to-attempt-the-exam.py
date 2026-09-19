Question:
Write a program that reads the attendance percentage A and the status of having a medical report M of a student and checks if any of the below conditions is satisfied:
A is greater than or equal to 75%.
M is equal to "Y".
Print "Allowed to write exam" if any of the given conditions is satisfied.
Otherwise, print "Cannot write exam".

Note:
• The last character of the attendance percentage A contains %.
• The remaining characters contain a Number.

Input:
80% Y

Output:
Allowed to write exam

Input:
60% N

Output:
Cannot write exam



.....
a=(input())
x=a[::-1]
y=x[1:]
new=(y[::-1])
new1=int(new)
b=input()
if new1>=75 or b=="Y":
    print("Allowed to write exam")
else:
    print("Cannot write exam")
