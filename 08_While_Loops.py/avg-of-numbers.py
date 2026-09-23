Question:
The average of N numbers from 1 can be calculated as:
Average = Sum of N numbers from 1 / Count of numbers in N

Example:
If N = 3
Average = (1 + 2 + 3) / 3 = 2.0

Input:
The input will be a single line containing an integer representing N.

Output:
The output should be a single line containing a float that is the average.



Python Code:
a = int(input())
sum = 0
counter = 1
while counter <= a:
    sum = sum + counter
    counter = counter + 1
avg = sum / a
print(avg)

