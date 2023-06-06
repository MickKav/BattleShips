from random import randint


# Function to create an empty board


def create_board():
    board = []
    for _ in range(6):
        board.append('O')
    return board

# Function to print the board


def print_board(board):
    for row in board:
        print(" ".join(row))

# Function to place the ships


def place_ships(board):
    ships = 0
    while ships < 5:
        ship_row = randint(0, 5)
        ship_col = randint(0, 5)
        if board[ship_row][ship_col] != 'S':
            board[ship_row][ship_col] = 'S'
            ships += 1

# Function that initializes and starts the game

def play_game():
    pass

