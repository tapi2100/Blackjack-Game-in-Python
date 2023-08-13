from art import logo
import random
import os

def clear():
  """Clear screen"""
  os.system('cls')

def draw_card():
  """Draws one card from a list of 1-11"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calc_score(cards):
  """Take a list of cards and return the sum"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(player_score, cpu_score):
  """Compare scores and calc win, lose, draw"""
  if player_score == cpu_score:
    return "Draw"
  elif cpu_score == 0:
    return "You lose, cpu has Blackjack"
  elif player_score == 0:
    return ("You win with a Blackjack!")
  elif player_score > 21:
    return ("Over the hilss and far away, you lose")
  elif cpu_score > 21:
    return ("Cpu is over 21, you win!")
  elif player_score > cpu_score:
    return("you win!")
  else:
    return ("You lose!")

def blackjack():
  """complete game of Blackjack"""
  print(logo)
  player_cards = []
  cpu_cards = []
  game_over = False

  for _ in range(2):
    player_cards.append(draw_card())
    cpu_cards.append(draw_card())

  while not game_over:
    player_score = calc_score(player_cards)
    cpu_score = calc_score(cpu_cards)
    print(f"Your cards: {player_cards} and score: {player_score}")
    print(f"Computer's first card: {cpu_cards[0]}")

    if player_score == 0 or cpu_score == 0 or player_score > 21:
      game_over = True
    else:
      draw_another = input("Would you like to draw another card? 'y' or 'n': ")
      if draw_another == "y":
        player_cards.append(draw_card())
      else:
        game_over = True

  while cpu_score != 0 and cpu_score < 17:
    cpu_cards.append(draw_card())
    cpu_score = calc_score(cpu_cards)

  print(f"Your final hand: {player_cards}, final score: {player_score}")
  print(f"Computer's final hand: {cpu_cards}, final score: {cpu_score}")
  print(compare(player_score, cpu_score))

while input("Do you want to play Blackjack? 'y' or 'n': ") == "y":
  clear()
  blackjack()