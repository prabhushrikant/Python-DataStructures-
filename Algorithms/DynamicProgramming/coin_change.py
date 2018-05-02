# example 1
# For example, for N = 4 and C = {1,2,3},
# there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4.
#
# example 2
# For N = 10 and C = {2, 5, 3, 6},
# there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.


# though this solution works , can't really optimize it since doesn't make use of
# substructure equation
def getWaysRec(n, c, sum1, comb, prev_denom):
    if sum1 == n:
        print comb
        return
    elif sum1 > n:
        return
    else:
        for i in range(len(c)):
            if c[i] >= prev_denom:
                comb1 = list(comb)
                comb1.append(c[i])
                getWaysRec(n,c,sum1+c[i], comb1, c[i])
        return

# recursive function making use of substructure property.
def getWaysRec2(n, c, i , sum1):
    if sum1 < 0:
        return 0
    elif sum1 == 0:
        return 1
    elif i < 0 and sum1 > 0:
        return 0
    else:
        #considering ith denomination, see we don't reduce i value because we have
        #infinite supply of that denomination, but we reduce the sum by c[i]
        a = getWaysRec2(n, c, i, sum1-c[i])
        #without considering ith denomination, hence sum remains unchanged.
        b = getWaysRec2(n, c, i-1, sum1)
        return a + b

# because it uses correct recursive function, we can now optimize it using DP
def getWaysDP(n, c):
    # denominations * sum
    dp = [[0 for x in range(n+1)] for y in range(len(c))]
    # print dp

    #so when sum is zero , there is only one way to make it, is by not geting any coin , i.e. 1 way
    #hence fill up first column of the dp , indicates zero sum as 1
    for i in range(len(c)):
        dp[i][0] = 1

    # print dp

    for i in range(len(c)):
        for j in range(1, n+1):
            # considering denom
            a = dp[i][j-c[i]] if j-c[i]>=0 else 0
            # not considering denom
            b = dp[i-1][j] if i >=1 else 0
            dp[i][j] = a + b

    # print dp
    return dp[len(c)-1][n]

def getWays(n, c):
    # return getWaysRec(n,sorted(c),0,[],c[0])
    # return getWaysRec2(n, c, len(c)-1, n)
    return getWaysDP(n, c)

    # Complete this function

n = 4 #target sum
m = 3 # length of denoms
c = [1,2,3] #denomination
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
print ways

n = 100 #target sum
m = 4 # length of denoms
c = [25,10,5,1] #denomination
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
print ways
