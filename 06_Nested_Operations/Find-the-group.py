Question:
Write a program that reads a number N and prints the group in which the given number N is present. The number N is always from 1 to 30.

Table:
Group 1 → 1, 7, 13, 19, 25
Group 2 → 2, 8, 14, 20, 26
Group 3 → 3, 9, 15, 21, 27
Group 4 → 4, 10, 16, 22, 28
Group 5 → 5, 11, 17, 23, 29
Group 6 → 6, 12, 18, 24, 30

Input:
The input will be a single line containing an integer representing N.

Output:
The output should be a single line containing a string that represents the group in which the given number N is present.



a=int(input())
if a==1 or a==7 or a==13 or a==19 or a==25:
    print("Group 1")
elif  a==2 or a==8 or a==14 or a==20 or a==26:
    print("Group 2")
elif  a==3 or a==9 or a==15 or a==21 or a==27:
    print("Group 3") 
elif  a==4 or a==10 or a==16 or a==22 or a==28:
    print("Group 4")
elif  a==5 or a==11 or a==17 or a==23 or a==29:
    print("Group 5")    
elif  a==6 or a==12 or a==18 or a==24 or a==30:
    print("Group 6")
