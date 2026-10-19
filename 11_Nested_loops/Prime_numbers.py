#Given a number N, write a program to print all the Prime Numbers from 1 to N.
CODE:
a=int(input())
if a>7:
    print(2)
    print(3)
    print(5)
    for i in range(1,a+1):
      if (6*i-1)%5 !=0:
        resul=6*i-1
        if resul<=a:
            print(resul)
      if (6*i+1)%5!=0:
        result=6*i+1
        if result<=a and result%7!=0:
            print(result)
        elif result==7:
            print(7)
else:
    for i in range(1,a+1):
      if (6*i-1)%5 !=0:
        resul=6*i-1
        if resul<=a:
            print(resul)
      if (6*i+1)%5!=0:
        result=6*i+1
        if result<=a and result%7!=0:
            print(result)
    
    
