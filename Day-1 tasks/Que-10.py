# Question 10: Imports, Functions, and Error Handling
# Question: Create a module containing a function calculate_power(base, exponent). Import the function into another file and use it to calculate the power of a number. If the exponent is negative, raise and handle a custom exception that prints "Negative Exponent Not Allowed".
# Input: 5, -2


from power_modul import calculate_power, NegativeExponentError

base = int(input("hello"))
exponent = int(input())

try:
    result = calculate_power(base, exponent)
    print(result)
except NegativeExponentError:
    print("Negative Exponent Not Allowed")
