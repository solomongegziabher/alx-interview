#!/usr/bin/python3
"""
Solution to the nqueens problem
"""
import sys


def is_safe(board, row, col, N):
    # Check if the current position is attacked by any other queen

    # Check the row
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check the upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens(N):
    # Create an empty board
    board = [['.' for _ in range(N)] for _ in range(N)]

    def backtrack(col):
        # Base case: all queens are placed
        if col >= N:
            print_solution(board)
            return

        # Try placing a queen in each row of the current column
        for row in range(N):
            if is_safe(board, row, col, N):
                # Place the queen
                board[row][col] = 'Q'

                # Recur for the next column
                backtrack(col + 1)

                # Remove the queen to backtrack
                board[row][col] = '.'

    # Start backtracking from the first column
    backtrack(0)


def print_solution(board):
    # Print the current board configuration
    for row in board:
        print(' '.join(row))
    print()

def main():
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the value of N from the command line argument
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N Queens problem
    solve_n_queens(N)


if __name__ == "__main__":
    main()
