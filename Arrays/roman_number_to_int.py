
roman_digits = {}
roman_digits['I']=1
roman_digits['V']=5
roman_digits['X']=10
roman_digits['L']=50
roman_digits['C']=100
roman_digits['D']=500
roman_digits['M']=1000

def roman_to_int(s):
    i = 0
    n = len(s)
    val = 0
    while i < n:
        if i+1 < n:
            v1 = roman_digits[s[i+1]]
            v = roman_digits[s[i]]
            if v < v1:
                val += v1-v
                i += 2
            else:
                val += v
                i += 1
        else:
            val += roman_digits[s[i]]
            i += 1
    return val

def int_to_roman(n):
    result = ""




if __name__ == '__main__':
    roman_number = "CXLI"
    print "roman number : " + roman_number + " int value: ",
    print roman_to_int(roman_number)

    roman_number = "CXXXXI"
    print "roman number : " + roman_number + " int value: ",
    print roman_to_int(roman_number)

    roman_number = "LXXIV"
    print "roman number : " + roman_number + " int value: ",
    print roman_to_int(roman_number)

    roman_number = "LXXVIII"
    print "roman number : " + roman_number + " int value: ",
    print roman_to_int(roman_number)

    roman_number = "XIX"
    print "roman number : " + roman_number + " int value: ",
    print roman_to_int(roman_number)

    roman_number = "MCMXCVI"
    print "roman number : " + roman_number + " int value: ",
    print roman_to_int(roman_number)