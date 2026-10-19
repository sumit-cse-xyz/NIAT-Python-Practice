# Palindrome - 2
# Program to check whether a string is palindrome or not (case-insensitive)

"""
README SECTION
---------------
🧩 Problem Statement:
Write a Python program to check whether a given string is a palindrome or not.
Treat uppercase and lowercase letters as the same when comparing.

📥 Input:
A single string.

📤 Output:
Print "True" if the string is palindrome, otherwise "False".

💻 Example:
Input:
Madam

Output:
True

✅ Status: Solved
🧠 Language: Python 3.10
👨‍💻 Author: Sumit Gupta (N26J01A0062)
---------------
"""

a = input().upper()
b = a[::-1].upper()

if a == b:
    print("True")
else:
    print("False")
