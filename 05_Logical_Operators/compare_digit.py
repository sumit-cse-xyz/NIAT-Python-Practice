COMPARE DIGITS

Description:
• If the number N is greater than 25.
• If the first digit of N is greater than the second digit of N.
Print the result as shown in sample output.

Input:
The input will be a single line containing a two-digit integer.

Output:
• The first line of output should be a boolean.
  True should be printed if the number is greater than 25, otherwise False should be printed.
• The second line of output should be a boolean.
  True should be printed if the first digit is greater than the second digit, otherwise False should be printed.




a=(input())
print(int(a)>25)
print(int(a[0])> int(a[1]))                                                                         
