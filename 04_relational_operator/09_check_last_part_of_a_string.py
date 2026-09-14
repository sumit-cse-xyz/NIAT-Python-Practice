```python
# Check Last Part of a String
# Problem Statement:
# Given a string, check whether it ends with a particular word.
#
# Input:
# A string and a word.
#
# Output:
# Print True or False.
#
# Example:
# Input:
# Hello World
# World
#
# Output:
# True

a = input()
b = input()

print(a[-len(b):] == b)
```
