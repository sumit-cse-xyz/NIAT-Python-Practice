#Question:- GIVEN TWO NUMBERS N AND K, WRITE A PROGRAM TO ORINT THE Kth LARGESR FACTOR OF THE GIVEN NUMBER N.
CODE//
a=int(input())
b=int(input())
count=0 
for i in range(a,0,-1):
    if a%i==0:
        count=count+1 
        if count==b:
            print(i)
            break
