"""Functional Battleship!"""

__author__ = "730607182"

import random


# inputting guess function
def input_guess(grid_size: int, row_or_column: str) -> int:
    """Takes grid size input, outputs the guess."""
    assert row_or_column == "row" or row_or_column == "column"
    while row_or_column == "row":
        row_guess: int = int(input("Guess a row: "))
        while row_guess > grid_size or row_guess < 1:
            row_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
            print(row_guess)
        return row_guess
    while row_or_column == "column":
        column_guess: int = int(input("Guess a column: "))
        while column_guess > grid_size or column_guess < 1:
            column_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
            print(column_guess)
        return column_guess


# printing grid function
def print_grid(size_grid: int, guessed_row: int, guessed_column: int, correct: bool) -> None:
    """Takes input of grid size, guessed row, guessed column and if its correct."""
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
    row_counter: int = 1
    while row_counter <= size_grid:
        current_row: str = ""
        column_counter: int = 1
        while column_counter <= size_grid:
            if row_counter == guessed_row and column_counter == guessed_column and correct is True:
                current_row += RED_BOX
            elif row_counter == guessed_row and column_counter == guessed_column and correct is False:
                current_row += WHITE_BOX
            else:
                current_row += BLUE_BOX
            column_counter += 1
        print(current_row)
        row_counter += 1


# checks if guess is correct
def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Checks if guess correct."""
    right_guess: bool = False
    if secret_row == row_guess and secret_column == column_guess:
        right_guess = True
    return right_guess


# main game function
def main(the_grid_size: int, the_secret_row: int, the_secret_column: int) -> None:
    """Main game function."""
    current_turn: int = 1
    max_turns: int = 5
    won: bool = False
    turns_left: int = max_turns - current_turn
    # game loop
    while turns_left >= 0 and not won:
        print(f"== Turn {current_turn}/{max_turns} ==")

        # prompt user for guesses
        the_row_guess: int = input_guess(the_grid_size, "row")
        the_column_guess: int = input_guess(the_grid_size, "column")
        
        # verify users guesses
        guess_correct = correct_guess(the_secret_row, the_secret_column, the_row_guess, the_column_guess)
        if guess_correct is True:
            print("Hit!")
            print(f"You won in {current_turn}/{max_turns} turns!")
            won = True
        else: 
            print("Miss!")
            turns_left -= 1
        
        # display grid
        print_grid(the_grid_size, the_row_guess, the_column_guess, won)

        current_turn += 1
    if won is False:
        print(f"X/{max_turns} - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, 1), random.randint(1, 1))