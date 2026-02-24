# Question 16: Number Guessing Game
"""
Create a number guessing game where the computer picks a random number between 1-100 and the user gets 7 attempts.
Rules:
1. After each guess, show if guess is too high or too low and attempts remaining
2. If correct: congratulate and show attempts used
3. If failed: reveal the number
4. Ask to play again

Hint: Use import random and random.randint(1, 100)
"""

import random

def guessing_game():
    num = random.randint(1, 100)
    attempts = 7
    attemps_used = 0

    print("Number Guessing game: You will be given 7 attempts to guess a number between 1-100")

    while attempts > 0:
        guess = int(input("Guess a number between 1-100: "))
        attemps_used += 1
        
        if guess == num:
            print(f"Congratulations!, you have guessed the number in {attemps_used} attemps")
            return 
        
        elif guess > num:
            print(f"Your guess is higher. You have {attempts} attemps remaining")
            attempts -= 1
    
        else:
            print(f"Your guess is lower. You have {attempts} attemps remaining")
            attempts -= 1
        
    
    print("Game Over! You didn't guess the number")
    print(f"The number was {num}")

while True:
    guessing_game()
    play = input("Do you want to play again (yes/no): ")
    if play.lower() != "yes" and play.lower() != "y":
        print("Thanks for playing")
        break