# Question 3: Grade Calculator
# Write a program that takes a student's marks and prints the grade using the following conditions:
# 90 and above → A
# 75 to 89 → B
# 50 to 74 → C
# Below 50 → Fail
# Input:82

marks = int(input("enter student mark:"))

if (marks >= 90):
    print("your grade is A")
elif (marks >= 75 and marks <= 89):
    print("your grade is B")
elif (marks >= 50 and marks <= 74):
    print("your grade is C")
else :
    print("your grade is Fail")