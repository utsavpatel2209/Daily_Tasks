# Python Programming Assignment

This document contains 10 Python programming questions covering conditional statements, type casting, functions, exception handling, modules, and match-case statements.

---

# Question 1: Largest of Three Numbers

## Problem Statement

Write a program that takes three integers as input and prints the largest among them using conditional statements.

### Input

```text
15
27
19
```

### Output

```text
27
```

---

# Question 2: Type Casting and Average

## Problem Statement

Take three numbers as input (they may contain decimal values). Convert them to `float` using type casting and print their average rounded to **2 decimal places**.

### Input

```text
12.5
15
17.5
```

### Output

```text
15.00
```

---

# Question 3: Grade Calculator

## Problem Statement

Write a program that takes a student's marks and prints the grade using the following conditions.

### Grade Criteria

| Marks | Grade |
|-------|-------|
| 90 and above | A |
| 75 – 89 | B |
| 50 – 74 | C |
| Below 50 | Fail |

### Input

```text
82
```

### Output

```text
B
```

---

# Question 4: Function to Count Vowels

## Problem Statement

Create a function that accepts a string and returns the number of vowels (`a`, `e`, `i`, `o`, `u`) present in it. Print the count.

### Input

```text
Programming
```

### Output

```text
3
```

---

# Question 5: Match Case - Month Days

## Problem Statement

Using a `match-case` statement, print the number of days in a month based on the month number.

### Conditions

- February → **28**
- April, June, September, November → **30**
- Remaining months → **31**

### Input

```text
9
```

### Output

```text
30
```

---

# Question 6: Safe Integer Conversion

## Problem Statement

Take a value as input and convert it into an integer using type casting. If the conversion fails, handle the exception and print **"Invalid Input"**.

### Input

```text
12A
```

### Output

```text
Invalid Input
```

---

# Question 7: Function with Multiple Parameters

## Problem Statement

Create a function `calculate_salary(basic, hra, bonus)` that returns the total salary. Take the three values as input and print the result.

### Input

```text
25000
5000
2000
```

### Output

```text
32000
```

---

# Question 8: Employee Bonus Calculator

## Problem Statement

Create a function `calculate_bonus(salary, experience)` that calculates an employee's bonus based on the following conditions.

### Bonus Criteria

| Experience | Bonus |
|------------|-------|
| ≥ 10 years | 20% of salary |
| ≥ 5 years and < 10 years | 10% of salary |
| < 5 years | 5% of salary |

Print the bonus amount.

### Input

```text
50000
7
```

### Output

```text
5000.0
```

---

# Question 9: Student Result Analyzer

## Problem Statement

Create a function `calculate_result(mark1, mark2, mark3)` that returns the student's result based on the average marks.

### Result Criteria

| Average Marks | Result |
|--------------|--------|
| ≥ 75 | Distinction |
| ≥ 60 and < 75 | First Class |
| ≥ 40 and < 60 | Second Class |
| < 40 | Fail |

### Additional Requirement

Use exception handling to ensure all marks are between **0** and **100**. If any mark is invalid, print:

```text
Invalid Marks
```

### Example 1

#### Input

```text
85
78
90
```

#### Output

```text
Distinction
```

### Example 2

#### Input

```text
95
120
80
```

#### Output

```text
Invalid Marks
```

---

# Question 10: Imports, Functions, and Error Handling

## Problem Statement

Create a module containing a function:

```python
calculate_power(base, exponent)
```

Import the function into another file and use it to calculate the power of a number.

If the exponent is negative, raise and handle a custom exception that prints:

```text
Negative Exponent Not Allowed
```

### Input

```text
5
-2
```

### Output

```text
Negative Exponent Not Allowed
```

---

# Topics Covered

- Conditional Statements (`if`, `elif`, `else`)
- Type Casting
- Functions
- Multiple Parameters
- String Processing
- `match-case`
- Exception Handling (`try-except`)
- Custom Exceptions
- Modules and Imports
- Percentage Calculations
- Average Calculation