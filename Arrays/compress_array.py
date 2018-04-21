# compress strings such as "1,2,3,6,8,9,10,12" into the string "1->3,6,8->10,12"

def compressString(s):

    if len(s) == 0:
        return ""

    result = []
    count = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            result.append(s[i])
            result.append(str(count)),
            count = 1

    result.append(s[i+1])
    result.append(str(count))

    r = "".join(result)
    return s if len(s) < len("".join(result)) else r

if __name__ == '__main__':
    s = "aaabbbcccc"
    print "string : " + s + " compressed string: ",
    r = compressString(s)
    print r

    s = "aaabbbc"
    print "string : " + s + " compressed string: ",
    r = compressString(s)
    print r

    s = "aaabc"
    print "string : " + s + " compressed string: ",
    r = compressString(s)
    print r

    s = "abc"
    print "string : " + s + " compressed string: ",
    r = compressString(s)
    print r

    s = "aaa"
    print "string : " + s + " compressed string: ",
    r = compressString(s)
    print r