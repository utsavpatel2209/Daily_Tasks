# Question 8: Employee Bonus Calculator
# Question: Create a function calculate_bonus(salary, experience) that calculates an employee's bonus based on the following conditions:
# ●	Experience ≥ 10 years → 20% of salary
# ●	Experience ≥ 5 years and < 10 years → 10% of salary
# ●	Experience < 5 years → 5% of salary
# Print the bonus amount.
# Input: 50000 , 7

def calculate_bonus(salary, experience):
    if (experience >= 10 ):
        bonus = salary * 20/100
    elif (experience >= 5 and experience <= 10):
        bonus = salary * 10/100
    elif (experience < 5):
        bonus = salary * 5/100
    return(bonus)    
 
salary = int(input("enter your salary:"))
experience = int(input("enter your experience:"))
bonus = calculate_bonus(salary, experience)
print("your bonus salary is:",bonus)