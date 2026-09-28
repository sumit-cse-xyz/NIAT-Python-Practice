Question:
Write a program that reads a string and prints the reverse of that string.

Input:
The input will be a single line containing a string.

Output:
The output should be a single line containing the reverse of the given string.

Explanation:
For example, if the given string is:
Hurray! We have won the match.
The output should be:
.hctam eht now evah eW !yarruH

Python Code:
a = input()
result = ""
for i in a:
    result = i + result
print(result)

Testcase:
Case 1
Input:
Hurray! We have won the match.
Output:
.hctam eht now evah eW !yarruH

Case 2
Input:
hello
Output:
olleh
