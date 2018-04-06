#code
BOARD_WIDTH = 999
BOARD_HEIGHT = 999

def convert_to_board(board, N, M):
    board_index = 0
    new_board = [[0 for x in range(M)] for y in range(N)] #note the values of M is width & N is height
    for x in range(N):
        for y in range(M):
            new_board[x][y] = board[board_index]
            board_index += 1
    return new_board

def print_board(board, N, M):
    print("printing {} * {} board".format(N,M))
    for x in range(N):
        for y in range(M):
            print(str(board[x][y]) + " "),
        print()
    print()

def print_board_flat(board, N, M):
    flat_board = ""
    for x in range(N):
        for y in range(M):
            flat_board += " " + str(board[x][y])
    print(flat_board.strip())

def flood_fill(board, r, c, oc, nc):

    # print ("processing - r:{},c:{}".format(r,c))

    if r < 0 or r >= BOARD_HEIGHT:
        return board
    elif c < 0 or c >= BOARD_WIDTH:
        return board
    elif board[r][c] != oc:
        # print ("r:{},c:{}".format(r,c))
        return board
    else:

        # paint with new color
        board[r][c] = nc

        # repeat for all adjascent cells
        # adjuscent cells
        flood_fill(board, r+1, c, oc, nc)
        flood_fill(board, r-1, c, oc, nc)
        flood_fill(board, r, c+1, oc, nc)
        flood_fill(board, r, c-1, oc, nc)

        #diagonal cells
        flood_fill(board, r+1, c+1, oc, nc)
        flood_fill(board, r-1, c+1, oc, nc)
        flood_fill(board, r+1, c-1, oc, nc)
        flood_fill(board, r-1, c-1, oc, nc)

        return board

if __name__ == "__main__":
    N_Tests = input()
    if N_Tests < 0:
        print("Invalid test case number")
    else:
        for test in range(N_Tests):
            N, M = raw_input().strip().split(' ')
            print("N:{}, M:{}".format(N,M))
            BOARD_HEIGHT = int(N)
            BOARD_WIDTH = int(M)
            B = raw_input().strip().split(' ')
            board = convert_to_board(B, int(N), int(M))
            print_board(board, int(N), int(M))
            X, Y, NC = raw_input().strip().split(' ')
            OC = board[int(X)][int(Y)]
            print("old color: {}".format(OC))
            print("paint with New color: {}".format(NC))
            filled_board = flood_fill(board, int(X), int(Y), OC, int(NC))
            print_board(filled_board, int(N), int(M))
            print_board_flat(filled_board, int(N), int(M))