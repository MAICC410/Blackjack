# Blackjack Game

Welcome to the Python Blackjack game! This project is a simple simulation of the Blackjack card game implemented in Python. It is designed to provide an interactive and enjoyable gaming experience right from your terminal. The game follows traditional Blackjack rules with an automated dealer.

## Features

- **Unlimited Deck Size:** The deck is virtual and unlimited, mimicking the effect of an infinite deck shuffle.
- **Standard Card Values:** 
  - Face cards (Jack, Queen, King) count as 10.
  - Aces can count as either 11 or 1, depending on the situation which best benefits the player.
- **Automated Dealer:** The computer plays as the dealer, following standard casino rules.
- **Interactive Play:** Players make decisions in real-time, choosing when to hit (take another card) or stand (end their turn).

## Game Rules

- The game starts by dealing two cards to both the player and the dealer. The dealer's first card is hidden.
- The player can then choose to 'Hit' to take another card or 'Stand' to hold their total.
- The goal is to get as close to 21 without going over. If your total exceeds 21, it's a 'bust,' and you lose the game.
- The dealer reveals their hidden card once the player stands and hits until their cards total 17 or higher.
- If you hold a total higher than the dealer's or the dealer busts, you win.

## How to Play

To start playing the game:
1. Clone this repository to your local machine.
2. Navigate to the cloned directory.
3. Run the Python script.

## Acknowledgments
This project was created as a part of the 100 days of code course from Udemy

```bash
git clone https://github.com/MAICC410/Blackjack.git
cd blackjack
python blackjack.py

