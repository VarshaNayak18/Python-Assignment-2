# Question 13: Sum and Average Calculator
"""
Ask the user how many numbers they want to add. Then take that many numbers as input using
a loop.
Calculate: 1. Sum 2. Average 3. Maximum number 4. Minimum number

Bonus: Add median, mode calculations
"""

# User input
n = int(input("How many numbers?: "))

# Calculate sum
sum = 0
nums = []
for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    nums.append(num)
    sum += num

print(f"Sum: {sum:g}")

# Average
avg = sum / n
print(f"Average: {avg:.2f}")

# Maximum and Minimum
maximum = nums[0]
minimum = nums[0]

for num in nums:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print(f"Maximum: {maximum:g}")

print(f"Minimum: {minimum:g}")

# Median 
nums.sort()

if n % 2 == 0:
    median = (nums[n//2 - 1] + nums[n//2]) / 2
else:
    median = nums[n//2]

print(f"Median: {median:g}")

# Mode
frequency = {}

for num in nums:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

max_freq = max(frequency.values())
mode = [key for key, value in frequency.items() if value == max_freq]

print(f"Mode: {mode}")