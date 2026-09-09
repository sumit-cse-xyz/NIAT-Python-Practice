#Question:
#Write a Python program that takes a person's name and age as input
#and prints the person's name and age in the given format.

#Input:
#The first line contains the person's name.
#The second line contains the person's age.

#Example Input:
#Sumit
#18

#Output:
#Print the name and age in the format:
#Sumit is 18 years old

#Example Output:
#Sumit is 18 years old


name = input()
age = int(input())

print(name + " is " + str(age) + " years" + " old")
