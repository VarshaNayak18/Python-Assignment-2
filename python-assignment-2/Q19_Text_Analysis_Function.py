# Question 19: Text Analysis Function
"""
Create the following text analysis functions:
1. count_words(text) - return number of words
2. count_vowels(text) - return number of vowels
3. count_consonants(text) - return number of consonants
4. reverse_text(text) - return reversed text
5. is_palindrome(text) - return True/False
6. remove_vowels(text) - return text without vowels
7. word_frequency(text) - return dictionary of word counts
8. longest_word(text) - return longest word
9. analyze_text(text) - calls all above functions and displays results
"""

def count_words(text):
    word_count = 0
    in_word = False
    for char in text:
        if char != " " and not in_word:
            word_count += 1
            in_word = True
        elif char == " ":
            in_word = False

    return word_count

def count_vowels(text):
    vowel_count = 0
    for char in text:
        if char.lower() in ["a", "e", "i", "o", "u"]:
            vowel_count += 1

    return vowel_count

def count_consonants(text):
    consonant_count = 0
    for char in text:
        if char not in ["a", "e", "i", "o", "u"] and char != " ":
            consonant_count += 1

    return consonant_count

def reverse_text(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text

    return reversed_text

def is_palindrome(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text

    if reversed_text.lower() == text.lower():
        return True
    else:
        return False
    
def remove_vowels(text):
    vowel_removed_text = ""
    for char in text:
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            vowel_removed_text += char 
    
    return vowel_removed_text

def word_frequency(text):
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

def longest_word(text):
    words = text.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    
    return f"{longest} ({len(longest)} letters)"

def analyze_text():
    text = input("Enter text: ")
    print("=== TEXT ANALYSIS ===")
    print(f"Words: {count_words(text)}")
    print(f"Vowels: {count_vowels(text)}")
    print(f"Consonants: {count_consonants(text)}")
    print(f"Reversed: {reverse_text(text)}")
    print(f"Palindrome: {'Yes' if is_palindrome(text) else 'No'}")
    print(f"Without vowels: {remove_vowels(text)}")
    print(f"Longest word: {longest_word(text)}")
    print(f"Word Frequency: {word_frequency(text)}")

analyze_text()