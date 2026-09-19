Question:
Write a program that reads a distance D in km and calculates the total score.

• For the first 40 km (0 - 40 km), the score for each km is 2.
• For the next 20 km (41 - 60 km), the score for each km is 4.
• For the next 60 km (61 - 120 km), the score for each km is 6.
• For the distance above 120 km, the score for each km is 8.
• Apart from the above scores, there is a bonus score of 50.

Input:
70

Output:
390


a=int(input())
if 0<=a<=40:
    print(a*2+50)
elif 41<=a<=60:
    print((a-40)*4 + 40*2+50)
elif 61<=a<=120:
    print((a-60)*6 +20*4 + 40*2 +50)
elif a>120:
    print((a-120)*8 + 60*6 +40*2 +20*4 +50)
    



 
