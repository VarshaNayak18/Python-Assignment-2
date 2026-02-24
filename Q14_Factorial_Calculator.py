# Question 14: Factorial Calculator
"""
Calculate factorial of a number using a loop. Factorial: n! = n x (n-1) x (n-2) x ... x 1
Requirements:
- Handle 0 and negative numbers
- Display step-by-step calculation
"""

# Take input from user
num = int(input("Enter a number: "))

# num is a negative integer
if num < 0:
    print("Factorial is not defined for negative numbers")

# num = 0
elif num == 0:
    print("0! = 1")

else:
    fact = 1
    for i in range(1, num+1):
        fact = fact *i
    s = " x ".join(str(i) for i in range(num, 0, -1))
    print(f"{num}! = {s} = {fact}")

