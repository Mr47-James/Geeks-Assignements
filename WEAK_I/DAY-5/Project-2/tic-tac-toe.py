def display_board(board):
    """Display the current Tic Tac Toe board."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def player_input(player, board):
    """Ask the player for a position and validate input."""
    while True:
        try:
            pos = int(input(f"Player {player} turn. Choose a position (1-9): ")) - 1
            if pos < 0 or pos > 8:
                print("Invalid position! Choose a number from 1 to 9.")
            elif board[pos] != " ":
                print("Position already taken! Choose another one.")
            else:
                return pos
        except ValueError:
            print("Invalid input! Please enter a number from 1 to 9.")


def check_win(board):
    """Check if a player has won. Returns 'X', 'O' or None."""
    win_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)              
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] != " ":
            return board[pos[0]]
    return None


def play():
    """Main function to run the game."""
    board = [" "] * 9
    current_player = "X"
    moves = 0

    print("Welcome to Tic Tac Toe!")
    display_board(board)

    while moves < 9:
        pos = player_input(current_player, board)
        board[pos] = current_player
        display_board(board)
        winner = check_win(board)
        if winner:
            print(f"Congratulations! Player {winner} wins!")
            return
        moves += 1
        current_player = "O" if current_player == "X" else "X"

    print("It's a tie!")

if __name__ == "__main__":
    play()
