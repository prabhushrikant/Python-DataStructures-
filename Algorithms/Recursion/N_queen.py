#!/bin/python

GRID_SIZE = 9999 #Reset in main function

def printBoard(board):
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            print str(board[r][c]) + " ",
        print

def initializeBoard(N):
    board = [[0 for r in range(N)] for c in range(N)]
    # printBoard(board)
    return board

def NQueen(board, col):
    if col == GRID_SIZE:
        printBoard(board) #found solution. either print or add it to the list.
        return True
    else:
         # Consider this column and try placing
         # this queen in all rows one by one
        for row in range(0, GRID_SIZE, 1):
            if isSafe(board, row, col):
                #place the queen here
                board[row][col] = 1

                if NQueen(board, col+1):
                    return True

                #backtrack & check another row.
                board[row][col] = 0

        #queen can't be placed in any of the rows
        return False

def isSafe(board ,row, col):

    #check if not any other queen is not placed in same row
    c = 0
    while c < col:
        if board[row][c] == 1:
            return False
        c += 1

    #check if not any other queen is not placed in same col
    r = 0
    while r < row:
        if board[r][col] == 1:
            return False
        r += 1

    #check that elements diagonals.
    r = row - 1
    c = col - 1
    # upper left diagonal
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
             return False
        r -= 1
        c -= 1

    # lower left diagonal
    r = row + 1
    c = col - 1
    while r < GRID_SIZE and c >= 0:
        if board[r][c] == 1:
            return False
        r += 1
        c -= 1

    return True

if __name__ == "__main__":
    N = int(raw_input().strip())
    if N < 0:
        print "Invalid amount specified."
    else:
        GRID_SIZE = N
        col = 0
        board = initializeBoard(N)
        if not NQueen(board, col):
            print "couldn't place queen"