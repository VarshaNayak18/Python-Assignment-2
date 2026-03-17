# Question 5: Bill Splitter
"""
Create a restaurant bill splitting program.
Inputs: Total bill amount, Number of people, Tax percentage, Tip percentage
Calculate and Display: Subtotal, Tax amount, Bill after tax, Tip amount, Total bill, Amount per
person
"""

# Take input from user
total_bill = float(input("Enter total bill: "))
total_people = int(input("Number of people: "))
tax_percent = float(input("Tax percentage: "))
tip_percent = float(input("Tip percentage: "))

# Calculation and display
print("=== BILL BREAKDOWN ===")

print(f"Subtotal: ₹{total_bill:.2f}")

total_tax = (tax_percent / 100) * total_bill
print(f"Tax ({tax_percent:g}%): ₹{total_tax:.2f}")

amount_after_tax = total_bill + total_tax
print(f"After tax: ₹{amount_after_tax:.2f}")

total_tip = (tip_percent / 100) * amount_after_tax
print(f"Tip ({tip_percent:g}%): ₹{total_tip:.2f}")

final_amount = total_bill + total_tax + total_tip
print(f"Total: ₹{final_amount:.2f}")

per_person = final_amount / total_people
print(f"Per person: ₹{per_person:.2f}")