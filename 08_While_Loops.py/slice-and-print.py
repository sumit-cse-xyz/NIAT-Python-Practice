Question:
Write a program that reads a string and prints each character of the given string on a new line.

Input:
The input will be a single line containing a string.

Output:
The output should be N lines, with each line containing one of the characters of the given string, where N is the length of the string.

Explanation:
For example, if the given string is shine,
• The length of the given string is 5.
• Each character of the string should be printed on a new line.
The output should be:
s
h
i
n
e

Python Code:
a = input()
count = 0
while count < len(a):
    slice = a[count]
    print(slice)
    count = count + 1


