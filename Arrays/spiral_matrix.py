def spiralOrder(m):
    """
    :type m: List[List[int]]
    :rtype: List[int]
    """
    f_r, l_r = 0, len(m)-1
    f_c, l_c = 0, len(m[0])-1
    i = 1

    res = []
    r,c = f_r, f_c
    while f_c <= l_c and f_r <= l_r: #equal to sign is needed for printing the middle element.
        # print first row

        # if f_c == l_c and f_r == l_r:
        #     print "wow"

        c = f_c  #f_c is changed after last while.
        # # while r <= f_r and c < l_c:
        # print "i : ", i
        # print "row limits: ", f_r, l_r
        # print "col limits: ", f_c, l_c

        while c <= l_c:
            # m[r][c] = i
            res.append(m[r][c])
            c += 1
            i += 1
        f_r += 1
        r = f_r
        c = c-1
        # i -= 1
        # print last column
        while r <= l_r:
            # m[r][c] = i
            res.append(m[r][c])
            r += 1
            i += 1
        l_c -= 1
        c = l_c
        r = r-1
        # i -= 1
        # print last row
        # second condition is need when first_row is still less or equal to last row
        # so that when f_r and l_r approach to each other they are not printed again.
        while c >= f_c and f_r <= l_r:
            # m[r][c] = i
            res.append(m[r][c])
            c -= 1
            i += 1
        l_r -= 1
        r = l_r
        c = c + 1
        # i -= 1
        # print first column
        while r >= f_r and f_c <= l_c:
            # m[r][c] = i
            res.append(m[r][c])
            r -= 1
            i += 1
        f_c += 1
        c = f_c
        r = r + 1
        # i -= 1
        # print "i in the end:", i

    return res


#driver script
# m = [[1,2,3],[4,5,6],[7,8,9]]
# res = spiralOrder(m)
# print res

m = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
res = spiralOrder(m)
print res