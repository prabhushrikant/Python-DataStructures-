#based on classic problem ...of longest common subsequence (no explaination needed)

#method 1 recursive

def LRS(a,b,i,j):

    if i == 0 or j == 0:
        #this is because once any string ends, there is no need to check for any commonality
        return 0
    else:
        # there is one more extra condition here than
        # LCS i.e. i and j should be same.
        if a[i] == b[j] and i != j:
            return 1 + LRS(a, b, i-1, j-1)
        else:
            #note you shouldn't add 1 here, to unecessarily increase the length of seq when things are not matching
            return max(LRS(a,b,i-1,j), LRS(a,b,i,j-1))

#method 2 dp

#how do we print the sequence though?

def print_repeating_seq(dp, a):
    i = len(a)
    j = len(a)
    res = ""
    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j-1] + 1:
            res += a[i-1]
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(res))

def LRS_DP(a,b):

    dp = [[0 for x in range(len(b)+1)] for y in range(len(a)+1)]

    #when a or b is empty no common subsequence can be found hence dp will be filled zero

    for j in range(len(b)+1):
        dp[0][j] = 0
    for i in range(len(a)+1):
        dp[i][0] = 0

    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):

            if a[i-1] == b[j-1] and i != j:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    res = print_repeating_seq(dp,a)

    return dp[len(a)][len(b)] , res

a = "abcdgh"
l, res = LRS_DP(a,a)
print "logest repeating subseq : " + res + " with length : " + str(l)

a = "AGGTAB"
l, res = LRS_DP(a,a)
print "logest repeating subseq : " + res + " with length : " + str(l)

a = "AABEBCDD"
l, res = LRS_DP(a,a)
print "logest repeating subseq : " + res + " with length : " + str(l)