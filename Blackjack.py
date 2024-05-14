

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


# Import random
import random

# Import and print Logo
from art import logo
print (logo)

# Create function to add card to hands
def another_card(hand):
  card = random.choice(cards)
  hand.append(card)
  

# Create function to caculate sum
def calculate_total(hand):
  total = sum(hand)
  aces = hand.count(11)

  while total > 21 and aces > 0:
    total -= 10
    aces -= 1

  return total



# Ask if they want to play

player_input = (input("Would you like to play? Yes or No "))
while player_input.lower() == "yes":
  player_hand = []
  dealer_hand = []
  total_player = 0
  total_dealer = 0
  
  #Build player and comp hands 
  while len(player_hand) < 2: 
    player_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))

  total_player = calculate_total(player_hand)
  total_dealer = calculate_total(dealer_hand)

  print(f"Your hand: {player_hand}. Player score: {total_player}")
  print(f"Dealer's hand: {dealer_hand[0]}")
  
  # Ask if they want another card
  more_cards = True
  while more_cards:
    answer = input("Type 'yes' to get another card, type 'no' to pass:")
    if answer == "yes":
      another_card(player_hand)
      total_player = calculate_total(player_hand)
      print (f"{player_hand}. Player score: {total_player}")
      if total_player > 21:
        more_cards = False
        print (f"Dealer's hand: {dealer_hand}. Dealer score: {total_dealer}")
        print("Bust!! You went over you lose.")
        if input("Play another again? (yes/no): ").lower() != "yes":
          break
        
    else:
      more_cards = False

      #Check Dealer hand
      total_dealer = calculate_total(dealer_hand)
      while total_dealer < 17:
        another_card(dealer_hand)
        total_dealer = calculate_total(dealer_hand)
      if total_dealer == total_player:
        print(f"Your hand: {player_hand}. Player score: {total_player}")
        print(f"Dealer's hand: {dealer_hand}. Dealer score: {total_dealer}")
        print("Draw")
      elif total_dealer < total_player:
        print(f"Your hand: {player_hand}. Player score: {total_player}")
        print(f"Dealer's hand: {dealer_hand}. Dealer score: {total_dealer}")
        print("You win.")
      elif total_dealer > 21:
        print(f"Your hand: {player_hand}. Player score: {total_player}")
        print(f"Dealer's hand: {dealer_hand}. Dealer score: {total_dealer}")
        print("You win.")
      elif total_dealer > total_player:
        print(f"Your hand: {player_hand}. Player score: {total_player}")
        print(f"Dealer's hand: {dealer_hand}. Dealer score: {total_dealer}")
        print("You lose.")
    
      #Check if player wants to continue playing
      if input("Play another again? (yes/no): ").lower() != "yes":
        break