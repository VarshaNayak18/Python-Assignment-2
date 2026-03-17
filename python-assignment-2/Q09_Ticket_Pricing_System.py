# Question 8: Ticket Pricing System
"""
Create a movie ticket pricing system.
Age-based Pricing:
Below 3: Free
3-12: ₹150 (Child)
13-59: ₹300 (Adult)
60+: ₹200 (Senior)
Day-based Discount:
Monday-Thursday: No discount
Friday-Sunday: 20% discount
Inputs: Age, Day of week, Number of tickets
Display base price, discount (if any), price after discount, and total amount.
"""

# Take input from user
people = int(input("Enter total number of people: "))

# Age Input and Ticket Price Calculation
price = 0
for i in range(people):
    age = int(input(f"Enter the age of person {i+1} in years: "))

    if age < 3 :
        price += 0

    elif age <= 12 :
        price += 150

    elif age <= 59 :
        price += 300

    else :
        price += 200

# User input of day
day = input("Enter the day: ")

print(f"Base Price: {price}")

if day.lower() in ["friday", "saturday", "sunday"]:
    print("You get 20 % Discount!")
    discount = (20 / 100) * price
    print(f"Discount amount: ₹{discount}")
    price_after_discount = price - discount
    print(f"Final price: ₹{price_after_discount}")

else:
    print("No discount applied")
    print(f"Final price: ₹{price}")