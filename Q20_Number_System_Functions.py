# Question 20: Number System Functions
"""
Create the following mathematical functions:
1. factorial(n) - return n!
2. is_prime(n) - return True if prime
3. fibonacci(n) - return nth Fibonacci number
4. sum_of_digits(n) - return sum of digits
5. reverse_number(n) - return number reversed
6. is_armstrong(n) - check if Armstrong number (e.g., 153 = 1³ + 5³ + 3³)
7. gcd(a, b) - greatest common divisor
8. lcm(a, b) - least common multiple
9. is_perfect_number(n) - sum of divisors equals n (e.g., 6 = 1+2+3)
10. math_menu() - menu to test all functions
Each function should be callable individually from the menu with appropriate user input.
"""

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact *i
        
    return fact

def is_prime(n):
    if n == 1:
        print("1 is neither prime nor composite")
    
    else:
        prime = True
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                prime = False
                break

        return prime

def fibonacci(n):
    first_num = 0
    second_num = 1
    sum = 0
    for i in range(2, n+1):
        sum = first_num + second_num
        first_num = second_num
        second_num = sum
    
    return sum

def sum_of_digits(n):
    sum = 0
    while n > 0:
        rem = n % 10
        n = n // 10
        sum += rem
    
    return sum

def reverse_number(n):
    reversed_num = ""
    while n > 0:
        rem = n % 10
        n = n // 10
        reversed_num += str(rem)

    return reversed_num

def is_armstrong(n):
    sum_cube = 0
    while n > 0:
        rem = n % 10
        n = n/10
        sum_cube += (rem * rem * rem)
    
    if sum_cube == n:
        return True
    
    else:
        return False

def gcd(a, b):
    if a < b:
        smaller = a
    else:
        smaller = b

    gcd = 1
    for i in range(1, smaller+1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return gcd

def lcm(a, b):
    if a > b:
        larger = a
    else:
        larger = b

    while True:
        if larger % a == 0 and larger % b == 0:
            return larger
        larger += 1

def is_perfect_number(n):
    sum = 0
    for i in range(1, (n//2)+1):
        if n % i == 0:
            sum += i
    
    if sum == n:
        return f"{n} is a perfect number"
    
    else:
        return f"{n} is not a perfect number"

# Main menu function
def math_menu():
    # Input from user
    n = int(input("Enter a number, n: "))
    a = int(input("Enter a number, a: "))
    b = int(input("Enter a number, b: "))

    if a <= 0 or b <=0 or n <= 0:
        print("Invalid input. Enter only positive integers as input")
    
    else:
        print("===MATHEMATICAL FUNCTIONS===")
        print(f"Factorial = {n}! = {factorial(n)}")
        print(f"Is {n} a prime number: {is_prime(n)}")
        print(f"{n}th Fibonacci number = {fibonacci(n)}")
        print(f"Sum of digits of {n} = {sum_of_digits(n)}")
        print(f"Reversed number = {reverse_number(n)}")
        print(f"Is {n} an armstrong number: {is_armstrong(n)}")
        print(f"Greatest Common Divisor (GCD) of {a} and {b} = {gcd(a, b)}")
        print(f"Least Common Multiple (LCM) of {a} and {b} = {lcm(a, b)}")
        print(f"Is {n} a perfect number: {is_perfect_number(n)}")
    
math_menu()