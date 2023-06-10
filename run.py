from random import randint

# Function to create an empty board


def create_board():
    board = []
    for _ in range(6):
        board.append(['O'] * 6)
    return board

# Function to print the board


def print_board(board):
    for row in board:
        print(" ".join(row))

# Function to place ships randomly on the board


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

    print("Welcome to Battleship!")

    while num_of_shots > 0:
        print("\nPlayer board:")
        print_board(player_board)

        # Get player's guess

        print(f"Shots remaining {num_of_shots}")
        print("Take a shot!")
        
        try:
            guess_row = int(input("Guess Row (0-5): "))
            guess_col = int(input("Guess Col (0-5): "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        if guess_row < 0 or guess_row > 5 or guess_col < 0 or guess_col > 5:
            print("Oops, your shot has just hit land!")
            continue

        if player_board[guess_row][guess_col] == 'X':
            print("You've already guessed that!")
            continue

        # Check player's guess against computer's board

        if computer_board[guess_row][guess_col] == 'S':
            print("Congratulations! You sank a ship!")
            player_board[guess_row][guess_col] = 'X'
            player_score += 1
            if player_score == 4:
                print("\nPlayer wins!")
                break
        else:
            print("Oops, you missed!")
            player_board[guess_row][guess_col] = 'X'

        num_of_shots -= 1

    if num_of_shots == 0:
        print("\nGame over! Out of shots.")
        print("Computer board:")
        print_board(computer_board)
        print("Better luck next time!")

# Play the game


play_game()
