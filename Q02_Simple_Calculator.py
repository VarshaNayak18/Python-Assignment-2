# Question 2: Simple Calculator
"""
1. Asks user for two numbers
2. Performs and displays: Addition, Subtraction, Multiplication, Division, Modulus,
Exponentiation
"""
# Ask user inputs
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Perform arithmetic operations
add = num1 + num2 # Addition
sub = num1 - num2 # Subtraction
mul = num1 * num2 # Multiplication
div = round(num1 / num2, 2) # Division
mod = num1 % num2 # Modulus
exp = num1 ** num2 # Exponential

# Display results
print("Results:")
print(f"{num1} + {num2} = {add}")
print(f"{num1} - {num2} = {sub}")
print(f"{num1} * {num2} = {mul}")
print(f"{num1} / {num2} = {div}")
print(f"{num1} % {num2} = {mod}")
print(f"{num1} ^ {num2} = {exp}")



# Output
"""
Enter first number: 15
Enter second number: 5
Results:
15 + 5 = 20
15 - 5 = 10
15 * 5 = 75
15 / 5 = 3.0
15 % 5 = 0
15 ^ 5 = 759375
"""