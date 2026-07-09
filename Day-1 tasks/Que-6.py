# Question 6: Safe Integer Conversion
# Question: Take a value as input and convert it into an integer using type casting. If the conversion fails, handle the exception and print "Invalid Input".
# Input:12A

try:
    value = input("enter any value:")
    number = int(value)
    print(number)    
except:
    print("invalid value")