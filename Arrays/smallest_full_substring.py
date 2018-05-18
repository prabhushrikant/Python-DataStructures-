def seen_all_chars_1(arr, sub_str):
    for ch in arr:
        if ch not in sub_str:
            return False
    return True

def get_shortest_unique_substring(arr, str):
    #pass # your code goes here
    #sliding window

    m = len(arr)
    res = ""
    curr_sub = ""
    min_length = 9999
    l = 0
    r = 0

    while r < len(str) and l <= r:

        # because sub string should be atleast len(arr) characters long.
        while (r-l+1) < m and r < len(str):
            r += 1

        if r-l+1 >= m:
            curr_sub = str[l:r+1]
            print curr_sub

            if len(curr_sub) < min_length:
                if seen_all_chars_1(arr, curr_sub):
                    min_length = len(curr_sub)
                    result = curr_sub
                    l += 1
                else:
                    r += 1
            else:
                l += 1

    print "result: " + result
    return result

arr = ['x','y','z']
str = 'xyyzyzyx'
print (get_shortest_unique_substring(arr, str))