import math

# Initialize the board
board = [[" " for _ in range(3)] for _ in range(3)]

# Function to print the board
def print_board():
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check if a player has won
def check_winner(player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def is_full():
    return all(board[row][col] != " " for row in range(3) for col in range(3))

# Minimax algorithm
def minimax(depth, is_maximizing):
    if check_winner("X"):
        return 10 - depth
    elif check_winner("O"):
        return depth - 10
    elif is_full():
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = max(best, minimax(depth + 1, False))
                    board[i][j] = " "
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = min(best, minimax(depth + 1, True))
                    board[i][j] = " "
        return best

# Function to find the best move for the AI
def best_move():
    best_val = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                move_val = minimax(0, False)
                board[i][j] = " "
                if move_val > best_val:
                    move = (i, j)
                    best_val = move_val
    return move

# Main game loop
while True:
    print_board()
    if is_full():
        print("It's a tie!")
        break
    row, col = map(int, input("Enter your move (row col): ").split())
    if board[row][col] == " ":
        board[row][col] = "O"
        if check_winner("O"):
            print_board()
            print("You win!")
            break
        if is_full():
            print_board()
            print("It's a tie!")
            break
        print("AI is making a move...")
        ai_move = best_move()
        board[ai_move[0]][ai_move[1]] = "X"
        if check_winner("X"):
            print_board()
            print("AI wins!")
            break
    else:
        print("Invalid move, try again.")

