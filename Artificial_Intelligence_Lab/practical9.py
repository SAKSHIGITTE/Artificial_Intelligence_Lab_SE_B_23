# Assume:
# Board is 3×3; players are X and O.
# X is the maximizer; O is minimizer.
# Utility: +1 if X wins; −1 if O wins; 0 if draw.

function minimax(board, player):
    if terminal(board):
        return utility(board)  # +1, −1, or 0

    if player == X:  # Maximizer
        bestVal = -∞
        for each legal_move in board:
            newBoard = apply_move(board, legal_move, X)
            val = minimax(newBoard, O)
            if val > bestVal:
                bestVal = val
        return bestVal
    else:  # player == O, minimizer
        bestVal = +∞
        for each legal_move in board:
            newBoard = apply_move(board, legal_move, O)
            val = minimax(newBoard, X)
            if val < bestVal:
                bestVal = val
        return bestVal

function findBestMove(board):
    bestMove = null
    bestVal = -∞
    for each legal_move in board:
        newBoard = apply_move(board, legal_move, X)
        val = minimax(newBoard, O)
        if val > bestVal:
            bestVal = val
            bestMove = legal_move
    return bestMove

