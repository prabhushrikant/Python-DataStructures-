import re
def reverse(a, k):
    n = len(a)
    for i in range(0, n, k):
        # print i
        j = i+k-1 if i+k-1 < n else n-1
        # print j
        while i < j:
            a[i],a[j] = a[j],a[i]
            i += 1
            j -= 1
        # print a
    return a

def remove_dup(a):
    result = ""
    i = 0
    while i < len(a):
        j = i + 1
        while j < len(a) and a[i] == a[j]:
            j += 1

        if j - i == 1:
            result += a[i]
        i=j
    return result

def maxProfit(days):
    b_index = 0
    s_index = b_index
    profit = 0

    i = 0
    while i < len(days):
        # print "day: "+ str(i)
        if days[b_index] <= days[i] and days[i]-days[b_index] > profit:
            s_index = i
            profit = days[i]-days[b_index]
            # print "Profit: " + str(profit)
        else:
            if profit > 0:
                print("("+str(b_index)+" "+str(s_index)+"), "),
                profit = 0
            b_index = i
            s_index = b_index
        i += 1

    if profit > 0:
        print("("+str(b_index)+", "+str(s_index)+"), "),

def retrieveMostFrequentlyUsedWords(literatureText, wordsToExclude):
    # WRITE YOUR CODE HERE
    # given_words = literatureText.split(' ')
    given_words = re.split('\s|,|`|\'| |\.|', literatureText.strip())
    # given_words = re.findall("(?i\b[a-z]+\b)",literatureText.strip())
    word_map = {}
    for w in given_words:
        w_ = w.lower()
        if w_ != '' and w_ not in wordsToExclude:
            if w_ in word_map:
                word_map[w_] += 1
            else:
                word_map[w_] = 1

    #find maximum occuring words in map
    max = -1
    for key, value in word_map.items():
        if value > max:
            max = value

    freq_words = []
    for key, value in word_map.items():
        if value == max:
            freq_words.append(key)

    return freq_words


def sortList(mylist):
    sorted_list = sorted(mylist)
    return sorted_list

def reorderLines(logFileSize, logfile):
    # WRITE YOUR CODE HERE
    id_map = {}
    content_words = []
    content_numbers = []
    for log_line in logfile:
        log_contents = log_line.split(' ')
        id = log_contents[0]
        content = log_contents[1:]
        id_map[content] = id
        if re.find('\d+',content):
            content_numbers.append(content)
        else:
            content_words.append(content)

    #sort the content_words lexicographically
    content_words_sorted = sorted(content_words)

    result = []
    for sorted_line in content_words_sorted:
        if sorted_line in id_map:
            result_line = id_map[sorted_line] + " " + sorted_line
            result.add(result_line)

    for number_line in content_numbers:
        if number_line in id_map:
            result_line = id_map[number_line] + " " + number_line
            result.add(result_line)

    return result


if __name__ == '__main__':

    print "wow"

    # days = [100, 180, 260, 310, 40, 535, 695]
    # days = [100, 40, 20, 60, 90, 15, 300]
    # days = [23, 13, 25, 29, 33, 19, 34, 45, 65, 67]

    # r = retrieveMostFrequentlyUsedWords("Rose is a flower red rose are flower", ["is", "are", "a"])
    # r = retrieveMostFrequentlyUsedWords("Jack and Jill went to the market to buy bread and cheese. Cheese is Jack's and Jill's favorite food.", ["and", "he", "the","to", "is"])

    # r = sortList(["jog mid pet", "alps cow bar"])

    # l = [["mi2","jog","mid","pet"]]
    # r = reorderLines(1, l)
    # print r
    # maxProfit(days)

    # # print remove_dup("acaaabbbacdddd")
    #
    # a = [0 for x in range(0,256)]
    #
    # s = "geeks for geeks"
    #
    # result = ""
    #
    # for c in s:
    #     if a[ord(c)] == 0:
    #         a[ord(c)] = 1
    #         result += c
    #
    # print result

# if __name__ == '__main__':
#
#     k = 3
#     a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     print "given",
#     print a,
#     print "k=" + str(k)
#     a_ = reverse(a, k)
#     print "revsd",
#     print a_
#
#     print
#     k = 5
#     b = [1, 2, 3, 4, 5, 6, 7, 8]
#     print "given",
#     print b,
#     print "k=" + str(k)
#     b_ = reverse(b, k)
#     print "revsd",
#     print b_