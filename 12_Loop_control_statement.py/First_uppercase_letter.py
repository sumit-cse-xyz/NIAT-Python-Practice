#question:- Given a string S, write a program to print the uppercase letter that appears forst in the string S.
Code:-
a=input()
for i in a:
    if i.isupper():
        print(i)
        break
