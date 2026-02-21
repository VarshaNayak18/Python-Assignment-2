# Question 4: Age Calculator
"""
Ask user for their birth year and calculate:
1. Current age
2. Age in months
3. Age in days (approx 365 days/year)
4. Age in hours
5. Age in minutes
6. Years until age 100
Bonus (+2 points): Ask for an exact birth date (day, month, year) and calculate more
precisely.
"""

# To extract today's date
from datetime import date
today = date.today()

# Take DOB(dd/mm/yyyy) input from user
dob_user = input("Enter your date of birth (dd/mm/yyyy): ")

# Extract day, month, year from dob_user
day, month, year = dob_user.split("/")

# Convert string to integer
day = int(day)
month = int(month)
year = int(year)

birth_date = date(year, month, day)

# Calculate difference
years = today.year - birth_date.year
months = today.month - birth_date.month
days = today.day - birth_date.day

if days < 0:
    months -= 1
    # Find number of days in previous month
    if today.month == 1:
        previous_month = 12
        previous_year = today.year - 1
    else:
        previous_month = today.month - 1
        previous_year = today.year
    
    days_in_prev_month = (date(previous_year, previous_month % 12 + 1, 1) - date(previous_year, previous_month, 1)).days
    
    days += days_in_prev_month
if months < 0:
    years -= 1
    months += 12

# Print age of user
print(f"Age: {years} years, {months} months, {days} days")
