def isSafe(board, row, col, n):
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
    # If all queens are placed, print the solution
    if row == n:
        printSolution(board, n)
        print()  # Adds a space between solutions (if more than one)
        return True

    # Flag to check if there is any solution
    res = False

    for col in range(n):
        if isSafe(board, row, col, n):
            board[row] = col
            res = solveNQueensUtil(board, row + 1, n) or res
            # Backtrack (remove queen from current position)
            board[row] = -1

    return res

def solveNQueens(n):
    board = [-1] * n
    if not solveNQueensUtil(board, 0, n):
        print("No solution exists.")
    else:
        print("Solutions found.")

# Example: Solving for n=4
n = 4
solveNQueens(n)

# Output: 
# . Q . . 
# . . . Q 
# Q . . . 
# . . Q . 

# . . Q . 
# Q . . . 
# . . . Q 
# . Q . . 

# Solutions found.