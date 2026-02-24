# Question 18: Calculator Functions
"""
Create a calculator using functions.
Required Functions:
1. add(a, b)
2. subtract(a, b)
3. multiply(a, b)
4. divide(a, b) - handle division by zero
5. modulus(a, b)
6. power(a, b)
7. calculator() - main function with menu
The calculator() function should display a menu, take user input, call the appropriate function, 
and display the result. Include an Exit option.

Bonus: Add square root, percentage functions
"""

def add(a, b):
    return a + b
    
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is undefined"
    
    return a / b
    
def modulus(a, b):
    if b == 0:
        return "Division by zero is undefined"
    
    return a % b
    
def power(a, b):
    return a ** b

def sqaure_root(n):
    return n ** 0.5

def percentage(num, den):
    if den == 0:
        return "Denominator cannot be zero"
    elif den < num:
        return "Numerator cannot be greater than denominator"
    
    percent = ( num / den) * 100
    return round(percent, 2)

# Main calculator function
def calculator():
    while True:
        print("MENU")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Square Root")
        print("8. Percentage")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "9":
            print("Exiting program")
            break

        if choice in ["1", "2", "3", "4", "5", "6"]:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Enter numbers only")
                continue

            if choice == "1":
                result = add(a, b)
            elif choice == "2":
                result = subtract(a, b)
            elif choice == "3":
                result = multiply(a, b)
            elif choice == "4":
                result = divide(a, b)
            elif choice == "5":
                result = modulus(a, b)
            elif choice == "6":
                result = power(a, b)

            print(f"Result: {result:.2f}")
        
        elif choice == "7":
            try:
                n = float(input("Enter number to find sqaure root: "))
            except ValueError:
                print("Invalid input. Enter numbers only")
                continue

            print(f"Result: {sqaure_root(n)}")

        elif choice == "8":
            try:
                num = float(input("Enter numerator: "))
                den = float(input("Enter denominator: "))
            except ValueError:
                print("Invalid input. Enter numbers only")
                continue

            print(f"Result: {percentage(num, den)} %")

        else:
            print("Invalid choice")

calculator()
    


    