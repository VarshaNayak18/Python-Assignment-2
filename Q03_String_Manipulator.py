# Question 3: String Manipulator
"""
Ask user for a sentence and display:
1. Original sentence
2. Total characters (with spaces)
3. Total characters (without spaces)
4. Total words
5. UPPERCASE
6. lowercase
7. Title Case
8. First word
9. Last word
10. Reversed sentence
"""

# Take a sentence as an input from user
sent = input("Enter a sentence: ")
print(f"Original: {sent}")

# Total characters (with spaces)
length = len(sent)
print(f"Characters (with spaces): {length}")

# Total characters (without spaces)
len_space_removed = 0
for i in sent:
    if i != " ":
        len_space_removed += 1
print(f"Characters (without spaces): {len_space_removed}")

# Total words
words = 1
for i in sent:
    if i == " ":
        words += 1
print(f"Words: {words}")

# Uppercase
print("UPPERCASE: ",sent.upper())

# Lowercase
print("lowercase: ",sent.lower())

# Title Case
print("Title Case: ",sent.title())

# First word
first_word = sent.strip().split()[0]
print(f"First word: {first_word}")

# Last word
last_word = sent.strip().split()[-1]
print(f"Last word: {last_word}")

# Reversed
reversed_sent = sent[::-1]
print(f"Reversed: {reversed_sent}")