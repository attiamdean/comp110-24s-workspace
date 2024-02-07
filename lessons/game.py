"""Number Guessing Games"""
from random import randint

SECRET: int = randint(1,10)
correct: bool = False
num_guesses: int = 0

while not correct: #correct == false
    guess: int = int(input("Guess a number :)"))
    if guess == SECRET:
        print(f"Correct! {guess} is the number!")
        #something to help us exit
        correct = True
    else:
        if guess > SECRET:
            print(f"{guess} is too high")
        if guess < SECRET:
            print(f"{guess} is too low")
        print("Guess again! ")
while num_guesses % 5 == 0 and num_guesses != 0:
    if num_guesses == 5
        pri



