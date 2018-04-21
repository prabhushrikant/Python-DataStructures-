def LPS(s, i, j, max_len, start_index):
    if len(s) == 0:
        return 0
    elif i >= len(s) or i > j:
        return max_len, start_index
    else:
        if s[i] == s[j]:
            if start_index == -1:
                start_index = i
            curr_max_len, curr_start_index = LPS(s, i+1, j-1, max_len+1, start_index)
            if curr_max_len > max_len:
                return curr_max_len, curr_start_index
            else:
                return max_len, start_index
        else:
            curr_max_len1, curr_start_index1 = LPS(s, i+1, j, max_len, start_index)
            curr_max_len2, curr_start_index2 = LPS(s, i, j-1, max_len, start_index)
            return_max_len = max(max_len, max(curr_max_len1, curr_max_len2))
            return_start_index = start_index
            if return_max_len == curr_max_len1:
                return_start_index = curr_max_len1
            elif return_max_len == curr_max_len2:
                return_start_index = curr_max_len2
            else:
                return_start_index = start_index
            return return_max_len, return_start_index

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """

    max_len, index = LPS(s, 0, len(s)-1, 0, -1)

    print max_len
    print index

if __name__ == '__main__':

    longestPalindrome("babad")