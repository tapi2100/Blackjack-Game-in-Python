from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if user_choice == "y":
  print(logo)
  one = cards[random.randint(0,12)]
  two = cards[random.randint(0,12)]
  score = one + two
  while score <= 21:
    print(f"Your cards: [{one}, {two}], current score: {one+two}")
    c_one = cards[random.randint(0,12)]
    print(f"Computer's first card: {c_one}")
    another = input("Type 'y' to get another card, type 'n' to pass: ")
    if another == "y":
      three = cards[random.randint(0,12)]
      score = score + three
      print(f"Your cards: [{one}, {two}, {three}], current score: {score}")
      # print(f"Computer's first card: {c_one}")
      c_two = cards[random.randint(0,12)]
      c_score = c_one + c_two
      print(f"Computer's final hand: [{c_one}, {c_two}], final score: {c_score}")
      if c_score > score:
        print("You lose!")
      else:
        print("You win!")
    else:
      c_two = cards[random.randint(0,12)]
      c_score = c_one + c_two
      print(f"Computer's final hand: [{c_one}, {c_two}], final score: {c_score}")
      if c_score > score:
        print("You lose!")
      else:
        print("You win!")
else:
  print("Well.. ok then =( ")


############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.