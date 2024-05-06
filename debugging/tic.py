#!/usr/bin/python3

# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))  # Join each cell in a row with " | " and print
        print("-" * 5)  # Print a line to separate rows

# Function to check if there is a winner
def check_winner(board):
    # Check rows for a win
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a win
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

# Function to play the Tic Tac Toe game
def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]  # Create an empty 3x3 board
    player = "X"  # Player X starts the game
     while not check_winner(board):
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if 0 <= row < 3 and 0 <= col < 3:  # Check if row and col are within range
                if board[row][col] == " ":
                    board[row][col] = player
                    player = "O" if player == "X" else "X"
                else:
                    print("That spot is already taken! Try again.")
            else:
                print("Invalid input! Please enter a number between 0 and 2.")
        except ValueError:
            print("Invalid input! Please enter a number between 0 and 2.")

    print_board(board)
    print("Player " + player + " wins!")

# Call the function to start the game
tic_tac_toe()
