# Question 7: Temperature Converter
"""
Create a temperature converter with a menu-based system supporting:
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius
5. Fahrenheit to Kelvin
6. Kelvin to Fahrenheit
7. Exit
"""

# Display all the options 
print("Menu- Temperature converter options available:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")
print("7. Exit")

while True:
    
    # Ask user to input choice
    choice = input("Enter your choice: ")

    if choice == "1":
        temp = float(input("Enter temperature in Celsius: "))
        new_temp = (temp * (9/5)) + 32
        print(f"{temp:g} °C = {new_temp:.2f} °F")

    elif choice == "2":
        temp = float(input("Enter temperature in Fahrenheit: "))
        new_temp = (temp -32) * (5/9) 
        print(f"{temp:g} °F = {new_temp:.2f} °C")
    
    elif choice == "3":
        temp = float(input("Enter temperature in Celsius: "))
        new_temp = temp + 273.15
        print(f"{temp:g} °C = {new_temp:.2f} K")

    elif choice == "4":
        temp = float(input("Enter temperature in Kelvin: "))
        new_temp = temp - 273.15
        print(f"{temp:g} K = {new_temp:.2f} °C")
    
    elif choice == "5":
        temp = float(input("Enter temperature in Fahrenheit: "))
        new_temp = ((temp -32) * (5/9)) + 273.15
        print(f"{temp:g} °F = {new_temp:.2f} K")
    
    elif choice == "6":
        temp = float(input("Enter temperature in Kelvin: "))
        new_temp = ((temp - 273.15) * (9/5)) + 32
        print(f"{temp:g} K = {new_temp:.2f} °F")

    elif choice == "7":
        print("Exiting Program")
        break

    else:
        print("Invalid Choice")