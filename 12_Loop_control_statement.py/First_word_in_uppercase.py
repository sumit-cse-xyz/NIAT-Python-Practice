#question:- Given a sentence S, write a program to print a new sentence by changing all letters of the word in the sentence S to upper case.
Code//
a=input()
result=""
for i in a:
    if i==" ":
        break
    result=result+i.upper()
print(result + a[len(result):])
