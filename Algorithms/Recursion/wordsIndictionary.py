


d = set()
d.add("i")
d.add("it")
d.add("is")
d.add("a")
d.add("wonder")
d.add("wonderful")
d.add("full")
d.add("life")

def is_word(s):
    if s in d:
        return True
    else:
        return False

def get_words(s, i):
    # print "word received: " + s[i:]
    if is_word(s[i:]):
        # print "result: " + s[i:]
        return [s[i:]]
    else:
        for p in range(i, len(s)):
            search_for = s[i:p+1]
            # print search_for
            if is_word(search_for):
                res = get_words(s, p+1)
                if len(res) > 0:
                    return [search_for] + res
        return []

result = get_words("itisawonderfullife",0)

print result
