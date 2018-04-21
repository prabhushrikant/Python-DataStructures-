# A message containing letters from A-Z is being encoded to numbers using the following mapping:
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.

# Example 1:
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
#
# Example 2:
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
#
# Example 3:
#
# Input: "206"
# Output: 1
# Explaination: It could be decoded as "U" (20), "F" (6)
#
# Example 4:
#
# Input: "2006"
# Output: 1
# Explanation: It could be not be decoded as anything because though 20 is valid , 06 is not valid encryption of any letter.
# because 0 is not valid number and 06 < 10 to be considered for 2 letter decoding.


class Solution(object):
    count = 0

    def is_valid(self, ss):
        if len(ss) <= 0:
            return False
        elif len(ss) == 1:
            num = int(ss)
            if num >= 1 and num <= 9:
                return True
            else:
                return False
        elif len(ss) == 2:
            num = int(ss)
            if num >= 10 and num <= 26:
                return True
            else:
                return False

    def numDecodingsRec(self, s, i):
        """
        :type s: str
        :rtype: int
        """
        if i >= len(s):
            return []
        elif i == len(s)-1:
            if self.is_valid(s[i]):
                self.count += 1
                return [s[i]]
        else:
            #this condition can't put it in else above, because it will return the recursion
            #without proceeding for last number.
            if i == len(s)-2:
                if self.is_valid(s[i:i+2]):
                    self.count += 1

            if self.is_valid(s[i]):
                self.numDecodingsRec(s,i+1)
            if len(s[i:]) >= 2 and self.is_valid(s[i:i+2]):
                self.numDecodingsRec(s,i+2)

    #this approach is more suitable for further improvisation using
    #memoisation or DP because it doesn't make use of global counter
    def numDecodingsRec2(self, s, i):
        """
        :type s: str
        :rtype: int
        """
        if i >= len(s):
            return 0
        elif i == len(s)-1:
            if self.is_valid(s[i]):
                return 1
        else:
            #this condition can't put it in else above, because it will return the recursion
            #without proceeding for last number.
            result = 0
            if i == len(s)-2:
                if self.is_valid(s[i:i+2]):
                    result = 1

            if self.is_valid(s[i]):
                result += self.numDecodingsRec2(s,i+1)
            if len(s[i:]) >= 2 and self.is_valid(s[i:i+2]):
                result += self.numDecodingsRec2(s,i+2)

            return result

    #improve method 2 to use memoisation
    memo = {}
    def numDecodingsRec_memo(self, s, i):
        """
        :type s: str
        :rtype: int
        """
        if i >= len(s):
            return 0
        elif i == len(s)-1:
            if self.is_valid(s[i]):
                return 1
        elif i in self.memo:
            return self.memo[i]
        else:
            #this condition can't put it in else above, because it will return the recursion
            #without proceeding for last number.
            result = 0
            if i == len(s)-2:
                if self.is_valid(s[i:i+2]):
                    result = 1

            if self.is_valid(s[i]):
                result += self.numDecodingsRec_memo(s,i+1)
            if len(s[i:]) >= 2 and self.is_valid(s[i:i+2]):
                result += self.numDecodingsRec_memo(s,i+2)

            self.memo[i] = result
            return self.memo[i]

    #improve method 3 to use DP (backward direction)
    #not working...
    def numDecodings_DP(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp=[0 for x in range(len(s)+1)]

        dp[len(s)] = 1

        for i in range(len(s)-1,-1,-1):
            if self.is_valid(s[i]):
                dp[i] = dp[i+1]
            else:
                dp[i] = 0

            if len(s[i:]) >= 2 and self.is_valid(s[i:i+2]):
                dp[i] += dp[i+2]

        # print dp
        return dp[0]
        # return dp[len(s)]

    #improve method 3 to use DP (forward direction)
    def numDecodings_DP1(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp=[0 for x in range(len(s)+1)]

        if self.is_valid(s[0]):
            dp[0] = 1

        for i in range(1, len(s)+1):
            if self.is_valid(s[i-1]):
                dp[i] = dp[i-1]
            else:
                dp[i] = 0

            if len(s[0:i]) >= 2 and self.is_valid(s[i-2:i]):
                dp[i] += dp[i-2]

        # print dp
        return dp[len(s)]
        # return dp[len(s)]

    def numDecodings(self,s):
        # method 1
        print "given string : " + s

        self.numDecodingsRec(s,0)
        print "answer method 1 :" + str(self.count)

        # method 2
        result = self.numDecodingsRec2(s,0)
        print "answer method 2 :" + str(result)

        # method 3
        result = self.numDecodingsRec_memo(s,0)
        print "answer method 3 :" + str(result)

        # method 4
        result = self.numDecodings_DP1(s)
        print "answer method 4 :" + str(result)

sol = Solution()
# sol.numDecodings("226")
# print sol.count

sol.numDecodings("226")

#follow up question , also put the number of different ways it can be decoded.
