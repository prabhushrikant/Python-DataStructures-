import re

def atoi(s):
    sum = 0

    if valid(s):

        sign = "+"
        sign = s[:1]
        if s[:1] == '-':
            sign = "-"

        power = len(s) - 1
        decimal_index = s.find('.')
        if decimal_index != -1:
            power = decimal_index - 1
        else:
            power = len(s)-1

        if s[:1] == '+' or s[:1] == '-':
            power -= 1
            s = s[1:]

        for c in s:
            if c == '.':
                break;
            sum += (ord(c) - ord('0')) * 10**power
            power -= 1

        if sign == "-":
            return sum * -1
        else:
            return sum
    else:
        raise ValueError("Invalid integer value passed")

def valid(s):
    if len(s) == 0:
        return False
    elif not containsNonNumeric(s):
        return False
    else:
        return True

def containsNonNumeric(s):

    # pattern for correct numeric string
    pattern = re.compile("^[-+]?\d+.?\d*$")

    if pattern.match(s):
        return True
    else:
        return False

if __name__ == '__main__':
    print str(atoi("34.56"))
    print str(atoi("-34.56"))
    print str(atoi("+34.56"))
    print str(atoi("34..56"))
    print str(atoi("shr.shr"))