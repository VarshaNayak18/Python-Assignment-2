# Question 17: Palindrome Checker
"""
Create a program that checks if a word/number is a palindrome (reads same forwards and backwards).
Requirements: Check words (ignore case), check numbers, display step-by-step verification.
"""

value = input("Enter word/number: ")

print(f"Original: {value}")

# Displays reverse of input word/number
reversed_value = ""
for char in value:
    reversed_value = char + reversed_value

# Check if word_num is palindrome
if value.lower() == reversed_value.lower():
    print("Result: PALINDROME")

else:
    print("Result: Not a PALINDROME")