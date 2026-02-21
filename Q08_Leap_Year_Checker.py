# Question 8: Leap Year Checker
"""
Create a program that checks if a year is a leap year.
Rules: A year is a leap year if divisible by 4 AND (NOT divisible by 100 OR divisible by 400).
"""

# Take year as input from the user
year = int(input("Enter the year: "))

# Leap year condition
if year % 400 == 0:
    print(f"Year: {year}")
    print(f"{year} is a leap year")
    print(f"Reason: {year} is divisible by 400")
    
elif year % 100 == 0:
    print(f"Year: {year}")
    print(f"{year} is not a leap year")
    print(f"Reason: {year} is divisible by 100 but not by 400")
    
elif year % 4 == 0:
    print(f"Year: {year}")
    print(f"{year} is a leap year")
    print(f"Reason: {year} is divisible by 4 but not by 100")
    
else:
    print(f"Year: {year}")
    print(f"{year} is a leap year")
    print(f"Reason: {year} is not divisible by 4")