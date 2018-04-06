# You are given two numbers and . You have to calculate the super digit of .
#
# is created when number is concatenated times. That is, if and , then .
#
# Input Format
#
# The first line contains two space separated integers, and .
#
# Constraints
#
# Output Format
#
# Output the super digit of , where is created as described above.
#
# Sample Input 0
#
# 148 3
#
# Sample Output 0
#
# 3
#
# Explanation 0
#
# Here and , so .
#
# super_digit(P) = super_digit(148148148)
# = super_digit(1+4+8+1+4+8+1+4+8)
# = super_digit(39)
# = super_digit(3+9)
# = super_digit(12)
# = super_digit(1+2)
# = super_digit(3)
# = 3.

#!/bin/python

import sys

# Approach 1 , fails for very large numbers.
# def digitSum(n, k):
#     # Complete this function
#     myStr = ""
#     while k > 0:
#         myStr += n
#         k -= 1
#     # print myStr
#     return superDigit(myStr)

# def superDigit(n):
#     if len(n) == 1:
#         return int(n)
#     else:
#         mySum = 0
#         for i in n:
#             mySum = mySum + int(i)
#         return superDigit(str(mySum))

# Approach 2 passes all test cases.

def getDigitSum(n):
    mySum = 0
    for i in n:
        mySum = mySum + int(i)
    return mySum

def digitSum(n, k):
    # Complete this function
    if len(str(n)) == 1:
        return getDigitSum(str(getDigitSum(str(n) * k)))
    else:
        mySum = getDigitSum(str(n))
        return digitSum(str(mySum), k)

if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [str(n), int(k)]
    result = digitSum(n, k)
    print result