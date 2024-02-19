"""one shot battleship!"""

__author__: str = "730607182"

# variables for rows, columns, where the secret rows and columns are
GRID_ROWS: int = 4
GRID_COLUMNS: int = 4
SECRET_ROW: int = 3
SECRET_COLUMN: int = 2


# variables for colored boxes
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# row and column guess variables, giving outputs if they are too high or low
row_guess: int = int(input("Guess a row: "))
while row_guess > GRID_ROWS:
    row_guess = int(input((f"The grid is only {GRID_ROWS} by {GRID_COLUMNS}. Try again: ")))
while row_guess < 0:
    row_guess = int(input((f"The grid is only {GRID_ROWS} by {GRID_COLUMNS}. Try again: ")))

column_guess: int = int(input("Guess a column: "))
while column_guess > GRID_COLUMNS: 
    column_guess = int(input(f"The grid is only {GRID_ROWS} by {GRID_COLUMNS}. Try again: "))
while column_guess < 0: 
    column_guess = int(input(f"The grid is only {GRID_ROWS} by {GRID_COLUMNS}. Try again: "))
# printing the grid

# making hitbox change colors depending on if it is a hit or not
hit_box: str = f"{WHITE_BOX}" or f"{RED_BOX}"
if row_guess == SECRET_ROW and column_guess == SECRET_COLUMN:
    hit_box = f"{RED_BOX}"
else:
    hit_box = f"{WHITE_BOX}"

# row counter variable
row_counter: int = 1

# making the boxes print
while row_counter <= GRID_ROWS:
    single_row_boxes: str = ""
    column_counter: int = 1
    if row_guess == row_counter:
        while column_counter <= GRID_COLUMNS:
            if column_guess == column_counter:
                single_row_boxes += hit_box
                column_counter += 1
            else:
                single_row_boxes += BLUE_BOX
                column_counter += 1
    else:
        while column_counter <= GRID_COLUMNS:
            single_row_boxes += BLUE_BOX
            column_counter += 1
    print(single_row_boxes)
    row_counter += 1               

# Hit or miss outputs
if row_guess == SECRET_ROW and column_guess == SECRET_COLUMN:
    print("Hit!")
elif row_guess == SECRET_ROW and column_guess != SECRET_COLUMN:
    print("Close! Correct row, wrong column.")
elif row_guess != SECRET_ROW and column_guess == SECRET_COLUMN:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")