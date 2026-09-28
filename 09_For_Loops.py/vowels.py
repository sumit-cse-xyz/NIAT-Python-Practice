Question:
Write a program that reads a string and prints the vowels in the string.

Input:
The input will be a single line containing a string.

Output:
The output should be a single line containing all vowels present in the given string.

Explanation:
For example, if the given string is "indian":
The vowels in the string are i, i, a.
So the output should be "iia".

Python Code:
a = input()
for i in a:
    if i in "aeiou":
        print(i, end="")

Testcase:
Case 1
Input:
indian
Output:
iia

Case 2
Input:
computer
Output:
oue
