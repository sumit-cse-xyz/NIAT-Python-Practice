Question:
Write a program that reads an amount A and prints the minimum number of 500, 50, 10 and 1 rupee notes required for the given amount.

Input:
The input will be a single line containing an integer representing the amount A.

Output:
The output should be a single line containing a string that has the number of 500, 50, 10 and 1 rupee notes required for the given amount A.

                                                                                                                    
if input=1543
  output= 500: 3 50: 0 10: 4 1:3
                                                                                                              

                                                                                                              
a=int(input())
r=int(a/500)
n=int((a-(500*r))/50)
d=int((a-(500*r)-(50*n))/10)
i=int(a-(500*r)-(50*n)-(10*d))
print("500"+": "+str(r)+" "+ "50"+": "+str(n)+" "+"10"+": "+str(d)+" "+"1"+": "+str(i))                                                                                                          
