# Given a digit string, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.

digit_dict = {
    1:[],
    2:['a','b','c'],
    3:['d','e','f'],
    4:['g','h','i'],
    5:['j','k','l'],
    6:['m','n','o'],
    7:['p','q','r','s'],
    8:['t','u', 'v'],
    9:['w','x','y','z'],
    0:[]
}

def letterCombinationsUtil(digits, i):
    if i == len(digits)-1:
        return digit_dict[int(digits[i])]
    else:
        result = []
        l = letterCombinationsUtil(digits, i+1)
        for c in digit_dict[int(digits[i])]:
            for s in l:
                result.append(c+s)
        return result

def letterCombinations_iterative(digits):
    #this initializing result with empty string is important for innermost loop to work for the first digit.
    result = [''] if digits else []
    for i in range(len(digits)):
        # print "processing :" + str(digits[i])
        curr_result = list()
        for c in digit_dict[int(digits[i])]:
            for r in result:
                curr_result.append(r+c)
        #update the result for next digit in input string.
        result = curr_result
    return result

if __name__ == '__main__':
    number = "23"
    print "recursive"
    print letterCombinationsUtil(number, 0)
    print "iterative"
    print letterCombinations_iterative(number)

    number = "20"
    print "recursive"
    print letterCombinationsUtil(number, 0)
    print "iterative"
    print letterCombinations_iterative(number)

    number = "120"
    print "recursive"
    print letterCombinationsUtil(number, 0)
    print "iterative"
    print letterCombinations_iterative(number)

    number = "10"
    print "recursive"
    print letterCombinationsUtil(number, 0)
    print "iterative"
    print letterCombinations_iterative(number)

    number = "234"
    print "recursive"
    print letterCombinationsUtil(number, 0)
    print "iterative"
    print letterCombinations_iterative(number)