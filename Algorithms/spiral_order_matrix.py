# def spiral_order_matrix(a,n,m,p,q):
#     right = True
#     down = True
#     j_fixed = False
#
#     i = 0
#     j = 0
#
#     while i < n or i >= m:
#         if not j_fixed:
#             while j < p and j >= q:
#                print str(a[i][j]) + ",",
#
#                if right:
#                    j += 1
#                else:
#                    j -= 1
#
#             if j >= p:
#                 j_fixed = True
#                 p -= 1
#                 m += 1
#                 right = not right
#                 j -= 1
#
#             elif j < q:
#                 j_fixed = True
#                 q += 1
#                 m += 1
#                 right = not right
#                 j += 1
#
#         if down:
#             i += 1
#         else:
#             i -= 1
#
#         if i >= n:
#             j_fixed = False
#             q += 1
#             n -= 1
#             down = not down
#             i -= 1
#             print str(a[i][j]) + ",",
#
#         elif i < m:
#             j_fixed = False
#             q += 1
#             m += 1
#             down = not down
#             i += 1
#             print str(a[i][j]) + ",",

def print_matrix(board, N, M):
    print("printing {} * {} board".format(N,M))
    for x in range(N):
        for y in range(M):
            print(str(board[x][y]) + " "),
        print
    print

if __name__=='__main__':

    N = 4
    M = 4
    a = [[0 for x in range(M)] for y in range(N)]

    a[0][0] = 1
    a[0][1] = 2
    a[0][2] = 3
    a[0][3] = 4

    a[1][0] = 5
    a[1][1] = 6
    a[1][2] = 7
    a[1][3] = 8

    a[2][0] = 9
    a[2][1] = 10
    a[2][2] = 11
    a[2][3] = 12

    a[3][0] = 13
    a[3][1] = 14
    a[3][2] = 15
    a[3][3] = 16

    print_matrix(a, M, N)

    # spiral_order_matrix(a,N,0,N,0)