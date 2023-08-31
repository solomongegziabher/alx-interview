#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    # Check if a queen can be placed at board[row][col]
   
    # Check upper row
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens(board, row):
    # Base case: All queens placed, print current configuration
    if row == N:
        print(board)
        return

    # Try placing queen in each column of current row
    for col in range(N):
        if is_safe(board, row, col):
            # Place queen at board[row][col]
            board[row][col] = 1

            # Recurse on the next row
            solve_nqueens(board, row + 1)

            # Backtrack: Remove queen from board[row][col]
            board[row][col] = 0

def nqueens(N):
    # Create an empty NxN board
    board = [[0] * N for _ in range(N)]

    # Solve the N Queens problem
    solve_nqueens(board, 0)

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Get the value of N from command line argument
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Check if N is at least 4
if N < 4:
    print("N must be at least 4")
    sys.exit(1)

# Solve and print the N Queens problem
nqueens(N)
