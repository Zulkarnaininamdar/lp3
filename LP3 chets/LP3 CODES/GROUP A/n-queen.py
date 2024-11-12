def is_safe(board, row, col, n):
    # Check for the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper-left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper-right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens(board, row, n):
    # Base case: if all queens are placed
    if row == n:
        return True
    
    # Try placing queen in all columns for the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            # Place queen
            board[row][col] = 1
            
            # Recursively place the next queen
            if solve_n_queens(board, row + 1, n):
                return True
            
            # Backtrack if placing queen leads to no solution
            board[row][col] = 0
    
    return False

def print_board(board, n):
    # Print the board
    for i in range(n):
        row = ""
        for j in range(n):
            if board[i][j] == 1:
                row += "Q "
            else:
                row += ". "
        print(row)

def n_queens(n):
    board = [[0] * n for _ in range(n)]  # Create an empty n x n board
    
    # Solve the n-Queens problem
    if solve_n_queens(board, 0, n):
        print("Solution found:")
        print_board(board, n)
    else:
        print("No solution exists")

# Driver code
n = int(input("Enter the value of n (size of the board): "))
n_queens(n)
