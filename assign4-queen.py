def isSafe(board, row, col):
    # Check the column for the same row
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True

def printSolution(board, n):
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

def solveNQueensUtil(board, row, n):
    if row == n: # If all queens are placed, print the solution
        printSolution(board, n)
        return True

    for col in range(n):
        if isSafe(board, row, col):
            board[row] = col
            if solveNQueensUtil(board, row + 1, n):
                return True
            board[row] = -1  # Backtrack (remove queen from current position)
    return False

def solveNQueens(n):
    board = [-1] * n
    if not solveNQueensUtil(board, 0, n):
        print("No solution exists.")

n = 4
solveNQueens(n)

# Output: 
# . Q . . 
# . . . Q 
# Q . . . 
# . . Q . 