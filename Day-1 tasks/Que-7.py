# Question 7: Function with Multiple Parameters
# Question: Create a function calculate_salary(basic, hra, bonus) that returns the total salary. Take the three values as input and print the result.
# Input: 25000, 5000, 2000

def calculate_salary():
    basic = int(input("enter basic salary:"))
    hra = int(input("enter your hra:"))
    bonus = int(input("enter your bonus:"))
    return (basic + hra + bonus)

total_salary = calculate_salary()
print("total salary is:",total_salary)