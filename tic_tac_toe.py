import random

# Tic Tac Toe

# Display the game board
def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

# Check if any player has won
def check_winner(board, mark):
    return (
        (board[7] == board[8] == board[9] == mark) or  # top row
        (board[4] == board[5] == board[6] == mark) or  # middle row
        (board[1] == board[2] == board[3] == mark) or  # bottom row
        (board[7] == board[4] == board[1] == mark) or  # left column
        (board[8] == board[5] == board[2] == mark) or  # middle column
        (board[9] == board[6] == board[3] == mark) or  # right column
        (board[7] == board[5] == board[3] == mark) or  # diagonal
        (board[9] == board[5] == board[1] == mark)     # diagonal
    )

# Check if the board is full (tie game)
def check_tie(board):
    return ' ' not in board[1:]

# Play the game against the computer
def play_game():
    board = [' '] * 10
    current_player = 'X'
    game_over = False

    while not game_over:
        display_board(board)
        
        if current_player == 'X':
            position = int(input("Player " + current_player + ", choose a position (1-9): "))
            
            if board[position] == ' ':
                board[position] = current_player
            else:
                print("That position is already occupied. Try again.")
                continue
        else:
            # Computer player's turn
            position = random.randint(1, 9)
            
            if board[position] == ' ':
                board[position] = current_player
            else:
                continue
        
        if check_winner(board, current_player):
            display_board(board)
            if current_player == 'X':
                print("Player " + current_player + " wins!")
            else:
                print("Computer wins!")
            game_over = True
        elif check_tie(board):
            display_board(board)
            print("It's a tie!")
            game_over = True
        
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()
