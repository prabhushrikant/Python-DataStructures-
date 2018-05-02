# You can perform the following operation on some string, :
#
# Capitalize zero or more of 's lowercase letters.
# Delete all of the remaining lowercase letters in .
#
# Given queries in the form of two strings, and , determine if it's possible to make equal to as described. If so, print YES on a new line. Otherwise, print NO.
#
# For example, given and a="AbcDE" and b="ABDE", in a we can convert b and delete c to match b.
# If a="AbcDE" and b="AFDE", matching is not possible because letters may only be capitalized or discarded, not changed or added.

# example 1
# 1
# daBcd
# ABC

# output:
# YES

# example 2
# 1
# AbcDE
# AFDE

# output:
# NO

# example 3
# 1
# FYyxu
# FY

# output:
# YES

#thinking ....solution can also be solved using hash maps. Create hashmap of characters from a and then check if all
# from b are in a with matching frequency, remove those from hashmap. After if hashmap still has any uppercase entries
# return NO else lowercase entries can be removed hence return YES
# O(N) and O(N) space.

#REcursive/DP approach.
# A simple DP approach works. For example, a = "aBbdD" b = "BBD" since the last character in a is upper case and last character in b is also upper case and both are equal, f(a,b) = f("aBbd","BB")
#
# Now d can never be made equal to B therfore- f("aBbd","BB") = f("aBb","BB")
#
# Now b can be capitalized to B,therfore we have two options - either capitalize b to B or dont capitalize b. f("aBb","BB") = f("aB","B") or f("aB","BB") #Note that this is the 'or' operator. f is a boolean value.
#
# if we have something like a = 'C' and b = 'D' then f(a,b) evaluates to False (boolean value).
#
# Lastly (for initialization of the dp array)-
#
# if a is non-empty and b is empty, then f(a,b) is True only if all the characters in a are lower case.
#
# if a is empty and b is non-empty, then f(a,b) is always False.
#
# if both are empty then f(a,b) = True

def abbreviationRec(a,b,i,j):
    if i == 0 and j == 0:
        return True
    elif i < 0 and j >= 0:
        return False
    elif i >= 0 and j < 0:
        # becasue i can be dropped.
        return True
    else:
        if a[i] == b[j]: #both are upercase and matching , check for rest of the strings
            return abbreviationRec(a, b , i-1, j-1)
        elif a[i].islower():
            if a[i] == b[j].lower():
                #a[i] can be upppercased and check remaining string or dropped (e.g. "FYy" and "FY")
                return abbreviationRec(a, b , i-1, j-1) or abbreviationRec(a, b, i-1, j)
            else:
                #a[i] needs to be dropped
                return abbreviationRec(a, b, i-1, j)
        else:
            #a[i] is uppercase and not matching with b[j] because first if failed.
            #we can't drop a[i] since it's upppercase hence False.
            return False

# dp approach
def abbreviationDP(a,b):
    dp = [[False for x in range(len(b)+1)] for y in range(len(a)+1)]
    # print dp

    dp[0][0] = True

    #it's not possible to make destination string or any length from an empty string
    for j in range(1,len(b)+1):
        dp[0][j] = False

    #it's possible to make destination string of zero length , if input characters can be dropped.ie if they contain
    #only lowercase letters.
    for i in range(1, len(a)+1):
        if a[i-1].islower():
            dp[i][0] = dp[i-1][0]
        else:
            dp[i][0] = False

    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1].islower():
                if a[i-1].lower() != b[j-1].lower():
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-1] or dp[i-1][j]
            else:
                if a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = False

    return dp[len(a)][len(b)]

#driver script
a = "KXzQ"
b = "k"
res1 = abbreviationRec(a,b,len(a)-1,len(b)-1)
res2 = abbreviationDP(a,b)
print "recursive: ",
print "YES" if res1 else "NO"
print "dp solution:",
print "YES" if res2 else "NO"