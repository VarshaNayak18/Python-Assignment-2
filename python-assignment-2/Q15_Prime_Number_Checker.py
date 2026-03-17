# Question 15: Prime Number Checker
"""
Part 1 (5 marks): Check if a single number is prime. Handle negative numbers, 0, 1, and 2.
Part 2 (2 marks): Find all prime numbers in a given range.
"""

# Part 1
num = int(input("Enter a number: "))

if num <= 0:
    print(f"{num} is not a prime number")

elif num == 1:
    print("1 is neither prime nor composite")

else:
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
    print(f"{num} is a Prime number" if is_prime else f"{num} is not a Prime Number")


# Part 2
start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

print(f"Prime numbers between {start} and {end} are:")

primes = []

for num in range(start, end+1):
    if num <= 1:
        continue
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            break
    else:
        primes.append(str(num))

print(", ".join(primes))