# given a string like
#
# 2[a]3[bc] ---> aabcbcbc
#
# input string can also contain embedded brackets:
#
# e.g  2[a3[c]] ----> acccaccc

# Note looks like difficult to be solved using recursion.
# think of the iterative solution using stack . might find it easier.

import re
class Solution(object):

    p = 0

    def isLetter(self,c):

        r = re.compile("[a-zA-Z]+")
        if r.match(c):
            return True
        else:
            return False

    def isDigit(self,c):
        r = re.compile("\d+")
        if r.match(c):
            return True
        else:
            return False

    def expandUtil(self,word, number):

        if number == "":
            return word
        else:
            result = ""
            for i in range(int(number)):
                result += word
            return result

    # Note - whenever in a recursive solution where you need a global index
    # you can assume that there is a simpler iterative solution is available.
    def expand_recursive(self, s, n):

        if self.p >= len(s):
            return ""
        else:
            number = ""
            word = ""
            while self.p < len(s):
                if self.isDigit(s[self.p]):
                    number += s[self.p]
                if s[self.p] == '[':
                    self.p += 1
                    word += self.expand(s, number)
                    #erase the number, after used in expand.
                    number = ""
                elif self.isLetter(s[self.p]):
                    word += s[self.p]
                elif s[self.p] == ']':
                    return self.expandUtil(word, n)
                self.p += 1
            return word

    def expand_iterative(self, s):
        stack = []
        i = 0
        number = ""
        word = ""
        result = ""
        #counts for opening and closing brackets
        o_count = 0
        c_count = 0
        #direction of the result if , opening brackets are more than closing ,
        #next result should be append back to the current.
        backword = False

        while i < len(s):
            if self.isDigit(s[i]):
                number += s[i]
            if self.isLetter(s[i]):
                word += s[i]
            if s[i] == '[':
                o_count += 1
                # push

                # Note : push the word first because it's always going to be a number before
                # the opening bracket hence word should go first
                if len(word) > 0:
                    stack.append(word)
                    # print stack
                    word = ""

                if len(number) > 0:
                    stack.append(number)
                    # print stack
                    number = ""

            elif s[i] == ']':
                c_count += 1
                # pop
                # print word
                if len(word) > 0:
                    p_word = word
                    word = ""
                else:
                    p_word = stack.pop()

                # print "number:" + number + "!!!"
                if len(number) > 0:
                    p_number = number
                    number = ""
                else:
                    p_number = stack.pop()

                if backword == False and o_count > c_count:
                    backword = True
                    result += self.expandUtil(p_word, p_number)
                else:
                    if backword:
                        p_word += result
                        result = ""
                        result += self.expandUtil(p_word, p_number)
                        if o_count > c_count:
                            backword = True
                        else:
                            backword = False
                    else:
                        result += self.expandUtil(p_word, p_number)

            i += 1
        return result

if __name__ == '__main__':
    s = "3[a2[c]]"
    print s
    sol = Solution()
    # print sol.expand_recursive(s,0)
    print sol.expand_iterative(s)

    s = "3[a]2[bc]"
    print s
    sol = Solution()
    # print sol.expand_recursive(s,0)
    print sol.expand_iterative(s)