"""EX01 - Simple Battleship - a cute step towards Battles"""

__author__ = "730607182"

""""printing a string of boxes"""

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

"""Player 1 input"""

User1_boat_location: int = int(input("Pick a secret boat location between 1 and 4:"))

if User1_boat_location > 4 : print("Error! " + str(User1_boat_location) + " too high!") + exit()
if User1_boat_location < 1 : print("Error! " + str(User1_boat_location) + " too low!") + exit()

"""Player 2 input"""

User2_guess1: int = int(input("Guess a number between 1 and 4:"))

Guessbox_color: str = str(WHITE_BOX) or str(RED_BOX)
if User1_boat_location == User2_guess1 : Guessbox_color = str(RED_BOX)
else: Guessbox_color == str (WHITE_BOX)

if User2_guess1 > 4 : print("Error! " + str(User2_guess1) + " too high!") + exit()
if User2_guess1 < 1 : print("Error! " + str(User2_guess1) + " too low!") + exit()

if User2_guess1 == 1 : print(Guessbox_color + BLUE_BOX + BLUE_BOX + BLUE_BOX)
if User2_guess1 == 2 : print(BLUE_BOX + Guessbox_color+ BLUE_BOX + BLUE_BOX)
if User2_guess1 == 3 : print(BLUE_BOX + BLUE_BOX + Guessbox_color + BLUE_BOX)
if User2_guess1 == 4 : print(BLUE_BOX + BLUE_BOX + BLUE_BOX + Guessbox_color)

"""Checking User input for Match"""

if User2_guess1 == User1_boat_location : print("Correct! You hit the ship.")

if User2_guess1 != User1_boat_location and User2_guess1 > 4 and User2_guess1 < 0 : print("Incorrect! You missed the ship.")
