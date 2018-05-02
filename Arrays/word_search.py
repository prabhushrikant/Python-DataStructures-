class Solution(object):
    def exist_rec(self, board, word, i, p, q, path):
        if p >= 0 and p < len(board) and q >=0 and q < len(board[0]) and i < len(word):
            found = False
            if board[p][q] != word[i]:
                return False

            #reaches here when word has matched so far.
            if (p, q) not in path:  # this looks if the current node is not already visited.
                path2 = list(path)
                path2.append((p, q))
                if board[p][q] == word[i]:
                    if i == len(word)-1:
                        return True

                # print i, word[i], path2

                #move in 4 adjascent places:
                x = p-1
                y = q
                while x <= p+1:
                    found = self.exist_rec(board, word, i+1, x, y, path2)
                    if found:
                        break
                    x += 1

                if not found:
                    x = p
                    y = q-1
                    while y <= q+1:
                        found = self.exist_rec(board, word, i+1, x, y, path2)
                        if found:
                            break
                        y += 1

                #if allowed to move in all 8 adjascent places use this
                # x = p-1
                # while x <= p+1:
                #     y = q-1
                #     while y <= q+1:
                #         found = self.exist_rec(board, word, i+1, x, y, path2)
                #         if found:
                #             break
                #         y += 1
                #     x += 1

                #return false if none of the adjascent found the word
                return found
            else:
                return
        else:
            return  #note it doesn't return true or false because, you want to backtrack
                    #try other options

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        #error checking here before calling
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.exist_rec(board, word, 0, i, j, []):
                    return True

        return False

#driver script
sol = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

word = "ABCB"
print word , str(sol.exist(board, word))

word = "SEE"
print word , str(sol.exist(board, word))

word = "ABCCEJ"
print word, str(sol.exist(board, word))

word = "ABCCED"
print word, str(sol.exist(board, word))