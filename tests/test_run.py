def reverse(a, k):
    n = len(a)
    for i in range(0, n, k):
        # print i
        j = i+k-1 if i+k-1 < n else n-1
        # print j
        while i < j:
            a[i],a[j] = a[j],a[i]
            i += 1
            j -= 1
        # print a
    return a

def remove_dup(a):
    result = ""
    i = 0
    while i < len(a):
        j = i + 1
        while j < len(a) and a[i] == a[j]:
            j += 1

        if j - i == 1:
            result += a[i]
        i=j
    return result

def maxProfit(days):
    b_index = 0
    s_index = b_index
    profit = 0

    i = 0
    while i < len(days):
        # print "day: "+ str(i)
        if days[b_index] <= days[i] and days[i]-days[b_index] > profit:
            s_index = i
            profit = days[i]-days[b_index]
            # print "Profit: " + str(profit)
        else:
            if profit > 0:
                print("("+str(b_index)+" "+str(s_index)+"), "),
                profit = 0
            b_index = i
            s_index = b_index
        i += 1

    if profit > 0:
        print("("+str(b_index)+", "+str(s_index)+"), "),


if __name__ == '__main__':

    # days = [100, 180, 260, 310, 40, 535, 695]
    days = [100, 40, 20, 60, 90, 15, 300]
    # days = [23, 13, 25, 29, 33, 19, 34, 45, 65, 67]

    maxProfit(days)

    # # print remove_dup("acaaabbbacdddd")
    #
    # a = [0 for x in range(0,256)]
    #
    # s = "geeks for geeks"
    #
    # result = ""
    #
    # for c in s:
    #     if a[ord(c)] == 0:
    #         a[ord(c)] = 1
    #         result += c
    #
    # print result

# if __name__ == '__main__':
#
#     k = 3
#     a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     print "given",
#     print a,
#     print "k=" + str(k)
#     a_ = reverse(a, k)
#     print "revsd",
#     print a_
#
#     print
#     k = 5
#     b = [1, 2, 3, 4, 5, 6, 7, 8]
#     print "given",
#     print b,
#     print "k=" + str(k)
#     b_ = reverse(b, k)
#     print "revsd",
#     print b_