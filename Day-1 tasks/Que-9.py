# Question 9: Student Result Analyzer
# Question: Create a function calculate_result(mark1, mark2, mark3) that returns:
# ●	"Distinction" if average ≥ 75
# ●	"First Class" if average ≥ 60 and < 75
# ●	"Second Class" if average ≥ 40 and < 60
# ●	"Fail" if average < 40
# Use exception handling to ensure all marks are between 0 and 100. If any mark is invalid, print "Invalid Marks".
# Input:85,78,90

def calculator_result(m1, m2, m3):
    valid = 0 <= m1 <= 100 and 0 <= m2 <= 100 and 0 <= m3 <= 100
    if (not valid):
        return "invalid Marks"
    avg = (m1 + m2 + m3)/3
    if (avg >= 75) :
        return "Destination"
    elif (avg >= 60 and avg <= 74):
        return "first class"
    elif (avg >= 40 and avg <= 59):
        return "second class"
    elif (avg <= 40):
        return "fail"

m1 = int(input("enter marks:"))
m2 = int(input("enter marks:"))
m3 = int(input("enter marks:"))
print ("your result is:", calculator_result(m1,m2,m3))