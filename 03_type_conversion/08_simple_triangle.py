# Simple Triangle

# Problem Statement:

# Given a number N, print a triangle pattern using *.

#

# Input:

# An integer N.

#

# Output:

# Print a triangle with N rows.

#

# Example:

# Input: 4

# Output:

# *

# **

# ***

# ****

n = int(input())

for i in range(1, n + 1):
print("*" * i)
