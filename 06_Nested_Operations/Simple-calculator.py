Question:
Write a program that reads an operator O, and two numbers A and B.
Print the result by doing arithmetic operations on A and B based on the operator O.

Operator | Arithmetic Operation | Represents
+ | A + B | Addition of A and B
- | A - B | Subtraction of B from A
* | A * B | Multiplication of A and B
/ | A / B | Division of A and B
% | A % B | Remainder when A is divided by B

Input:
+
3
5

Output:
8


i1=input()
i2=int(input())
i3=int(input())
if i1=="+":
 print(i3+i2)
elif i1=="-" :
 print(i2-i3)
elif i1=="*" :
 print(i2*i3)
elif i1=="/" :
 print(i2/i3) 
elif i1=="%" :
 print(i2%i3) 
 
