# Question 12: Multiplication Table Generator
# Create a program that asks the user for a number and a range, then displays the multiplication
# table.

# Take user input
num = int(input("Enter number: "))
r = int(input("Enter range (end): "))

print(f"Multiplication Table of {num}")
for i in range(1, r+1):
    print(f"{num} x {i} = {num * i}")


# Bonus (+3 points): Create a full multiplication table (1-10 for all numbers 1-10) in grid format.

print("Multiplication table grid for numbers from 1-10")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end="")
    print()