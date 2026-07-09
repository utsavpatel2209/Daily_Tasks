# Question 1: Largest of Three Numbers
# Write a program that takes three integers as input and prints the largest among them using conditional statements.
# input:15,27,19

a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))

if a > b and a > c :
    print("your greater number is a:", a)
elif b>c and b > c :
    print("your greater number is b:", b)
else :
    print("your greater number is c:", c)