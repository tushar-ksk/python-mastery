import random

def print_board(board):
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("---+---+---")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("---+---+---")
    print(f" {board[1]} | {board[2]} | {board[3]} ")

def is_winner(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))

def get_player_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move)] == ' ':
            return int(move)
        else:
            print("Invalid move. Please choose an empty space between 1 and 9.")

def get_computer_move(board, computer_marker, player_marker):
    # Check if computer can win
    for i in range(1, 10):
        board_copy = board[:]
        if board_copy[i] == ' ':
            board_copy[i] = computer_marker
            if is_winner(board_copy, computer_marker):
                return i

    # Check if player can win and block them
    for i in range(1, 10):
        board_copy = board[:]
        if board_copy[i] == ' ':
            board_copy[i] = player_marker
            if is_winner(board_copy, player_marker):
                return i

    # Try to take the center
    if board[5] == ' ':
        return 5

    # Take a corner
    corners = [1, 3, 7, 9]
    available_corners = [corner for corner in corners if board[corner] == ' ']
    if available_corners:
        return random.choice(available_corners)

    # Take a side
    sides = [2, 4, 6, 8]
    available_sides = [side for side in sides if board[side] == ' ']
    if available_sides:
        return random.choice(available_sides)

def tic_tac_toe():
    print("Welcome to Tic Tac Toe!")
    while True:
        board = [' '] * 10
        player_marker = ''
        computer_marker = ''

        while player_marker not in ('X', 'O'):
            player_marker = input("Do you want to be X or O? ").upper()

        if player_marker == 'X':
            computer_marker = 'O'
        else:
            computer_marker = 'X'

        turn = random.choice(['player', 'computer'])
        print(f"The {turn} goes first.")

        game_over = False
        while not game_over:
            if turn == 'player':
                print_board(board)
                move = get_player_move(board)
                board[move] = player_marker
                if is_winner(board, player_marker):
                    print_board(board)
                    print("Congratulations! You won!")
                    game_over = True
                elif ' ' not in board[1:]:
                    print_board(board)
                    print("It's a tie!")
                    game_over = True
                else:
                    turn = 'computer'
            else:
                move = get_computer_move(board, computer_marker, player_marker)
                board[move] = computer_marker
                print(f"Computer placed {computer_marker} on position {move}.")
                if is_winner(board, computer_marker):
                    print_board(board)
                    print("Computer wins! Better luck next time.")
                    game_over = True
                elif ' ' not in board[1:]:
                    print_board(board)
                    print("It's a tie!")
                    game_over = True
                else:
                    turn = 'player'

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

if __name__ == "__main__":
    tic_tac_toe()
