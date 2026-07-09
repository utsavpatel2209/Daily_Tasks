# Question 5: Match Case - Month Days
# Question: Using a match-case statement, print the number of days in a month based on the month number.
# ●	February → 28
# ●	April, June, September, November → 30
# ●	Remaining months → 31
# Input: 9

month = int(input("enter month number:"))

match month:
    case 2:
        print(28)
    case 4 | 6 | 9 | 11:
        print(30)
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print(31)
    case _:
        print("invalid number")
