# Done by Carlos Amaral (2021/03/09)

from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list

import random

print(logo)
print("Welcome to the hangman game!!")

# Choose a random word from the word list
chosen_word = random.choice(word_list)
# Get the total length of the word
word_length = len(chosen_word)

# Initialize the game and the initial lives
lives = 6
end_of_game = False

print("\n")

# Create blank spaces for the words
display = []
for letter in chosen_word:
  display += '_'
print(display)

# Build the game
while not end_of_game:
  guess = input("Guess a letter: ").lower()

  # Check if user is repeating a guessed word
  if guess in display:
    print(f"{guess} has already been entered! Try again!")
  # Check if the letter user gave matches the word
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter

  # Check if the user is wrong
  if guess not in chosen_word:
    print(f"Sorry, {guess} is not present in the word!")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print(f"You loose! The correct word was {chosen_word}")

  # Join all the elements in the list and turn it into a string.
  print(f"{' '.join(display)}")

  # Check if the user has got all letters
  if "_" not in display:
    end_of_game = True
    print("You win.")


  print(stages[lives])

