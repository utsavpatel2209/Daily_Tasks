# Question 10: Imports, Functions, and Error Handling
# Question: Create a module containing a function calculate_power(base, exponent). Import the function into another file and use it to calculate the power of a number. If the exponent is negative, raise and handle a custom exception that prints "Negative Exponent Not Allowed".
# Input: 5 , -2


class NegativeExponentError(Exception):
    pass

def calculate_power(base, exponent):
    if exponent < 0:
        raise NegativeExponentError("Negative Exponent Not Allowed")
    return base ** exponent