# write program to check if set of parenthesis is a valid.
# e.g. "{()}" or "[](){}" is valid
# but "}()" is not or "{{{()}}}}" is not valid
# string only contains 3 types of parenthesis "[]" or "{}" or "()"

class Solution(object):

    def valid_parenthisis(self,s):

        #algorithm, if found opening parenthesis put it onto the stack.
        #while end of the input string :
        #if found closing parenthisis:
        #  pop from the stack if not empty, else return false
        #  check popped closing bracket is of same kind , else return false

        #in the end if there is still items in stack.
        # return false
        #else return true.

        print "algo to be completed."