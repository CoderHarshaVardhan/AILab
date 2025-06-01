def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False
        if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:
            return False
        if col + (row - i) < len(board) and board[i][col + (row - i)] == 1:
            return False
    return True

def solve_n_queens(board, row=0):
    if row == len(board):
        print_board(board)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_n_queens(board, row + 1)
            board[row][col] = 0  

n = 8
board = [[0 for _ in range(n)] for _ in range(n)]

solve_n_queens(board)
