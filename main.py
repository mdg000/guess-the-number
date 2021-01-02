# 100 Days Code 
# Guess the number

import random
from art import logo

print(logo)

answer = random.randint(1, 100)
# functions
# sets the difficulty
def mode(difficulity):
  if difficulity == 'easy':
    lives = 10
  elif difficulity == 'hard':
    lives = 5
  return lives

# checks if guess is correct
def check_guess(guess, number):
  if guessed_num > number:
    return "Too High.\nGuess again."
  elif guessed_num < number:
    return "Too Low.\nGuess again."

# game start    
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulity = input("Choose a difficulty. Type 'easy' or 'hard': ")
lives_remaining = mode(difficulity)

# main game loop
game_won = False
while lives_remaining > 0 and game_won == False:

  print(f"You have {lives_remaining} attempt remaining to guess the number")
  guessed_num = (int(input("Make a guess: ")))
  result = check_guess(guess=guessed_num, number=answer)
  # ends game if guess is correct
  if guessed_num == answer:
    print(f"You got it! The answer was {answer}.")
    break

  print(result)
  lives_remaining -= 1

if lives_remaining == 0:
  print("You've run out of guesses, you lose.")