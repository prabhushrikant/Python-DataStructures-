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

#generate square matrix of size n , filled up spirally.
#Just replace assignments with print in while loops below for printing spirally
def generateMatrix(self, n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    m = [[-1 for x in range(n)] for y in range(n)]
    print m

    f_r, l_r = 0, n-1
    f_c, l_c = 0, n-1
    i = 1
    # while i <= n:

    p = 1
    r,c = f_r, f_c
    while i <= n*n:
        # print first row
        c = f_c
        # while r <= f_r and c < l_c:
        print "i : ", i
        print "row limits: ", f_r, l_r
        print "col limits: ", f_c, l_c

        while c <= l_c:
            m[r][c] = i
            c += 1
            i += 1
        f_r += 1
        r = f_r
        c = c-1
        # i -= 1
        # print last column
        while r <= l_r:
            m[r][c] = i
            r += 1
            i += 1
        l_c -= 1
        c = l_c
        r = r-1
        # i -= 1
        # print last row
        while c >= f_c:
            m[r][c] = i
            c -= 1
            i += 1
        l_r -= 1
        r = l_r
        c = c + 1
        # i -= 1
        # print first column
        while r >= f_r:
            m[r][c] = i
            r -= 1
            i += 1
        f_c += 1
        c = f_c
        r = r + 1
        # i -= 1
        print "i in the end:", i


    print m
    return m

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