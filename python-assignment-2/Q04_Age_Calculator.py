# Question 4: Age Calculator
"""
Ask user for their birth year and calculate:
1. Current age
2. Age in months
3. Age in days (approx 365 days/year)
4. Age in hours
5. Age in minutes
6. Years until age 100
Bonus (+2 points): Ask for an exact birth date (day, month, year) and calculate more precisely.
"""

# Take today's date (dd/mm/yyyy) input from user
date_today = input("Enter today's date (dd/mm/yyyy): ")

# Take DOB (dd/mm/yyyy) input from user
dob_user = input("Enter your date of birth (dd/mm/yyyy): ")

# Extract day, month, year from input and convert it to integer
day, month, year = map(int, dob_user.split("/"))
day_today, month_today, year_today = map(int, date_today.split("/"))

# Calculate difference
years = year_today - year
months = month_today - month
days = day_today - day

# No of days in each month
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Check if leap year 
if (year_today % 4 == 0 and year_today % 100 != 0) or (year_today % 400 == 0):
    days_in_month[1] = 29

# If days are negative
if days < 0:
    months -= 1
    days += days_in_month[month_today - 2]

# If months are negative
if months < 0:
    years -= 1
    months += 12

# Current age
print(f"Current age: {years} years, {months} months, {days} days")

# Age in months - approx (excluding days)
age_in_months = (years * 12) + months
print(f"Age in months: {age_in_months}")

# Age in days
age_in_days = (years * 365) + (months * 30) + days
print(f"Age in days: {age_in_days}")

# Age in hours 
age_in_hours = (years * 8760) + (months * 720) + (days * 24)
print(f"Age in hours: {age_in_hours}")

# Age in minutes 
age_in_minutes = (years * 525600) + (months * 43200) + (days * 1440)
print(f"Age in minutes: {age_in_minutes}")

# Years until age 100
years_until_100 = 100 - years
print(f"Years until age 100: {years_until_100}")