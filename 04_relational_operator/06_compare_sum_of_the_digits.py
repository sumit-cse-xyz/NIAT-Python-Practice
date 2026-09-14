```python
# Compare Sum of the Digits
# Problem Statement:
# Given two numbers, compare the sum of their digits.
#
# Input:
# Two three-digit numbers.
#
# Output:
# Print True if the sum of digits of the first number is greater
# than the sum of digits of the second number.
#
# Example:
# Input:
# 123
# 111
#
# Output:
# True

a = (input())
b = (input())
a=int(a[0])+int(a[1])+int(a[3])
b=int(b[0])+int(b[1])+int(b[3])
print(a>b)
