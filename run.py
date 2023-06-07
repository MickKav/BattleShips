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
    player_board = create_board()
    computer_board = create_board()
    place_ships(computer_board)
    num_of_shots = 10
    player_score = 0

    print(Welcome to BattleShips!)
    print(Where you have 10 shots to take down the hidden enemy ships)

    while num_of_shots > 0:
        print("\nPlayer Board:")
        print_board(player_board)

        #Get players guess
        try:
            guess_row = int(input("Guess Row (0-5): "))
            guess_col = int(input("Guess Col (0-5): "))
        except ValueError:
            print("Invalid input. Please enter numbers")
            continue
