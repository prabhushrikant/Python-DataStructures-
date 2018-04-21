def intToRoman(number):
    """
    :type num: int
    :rtype: str
    """
    roman_dict = {1:"I",
                  4:"IV",
                  5:"V",
                  9:"IX",
                  10:"X",
                  40:"XL",
                  50:"L",
                  90:"XC",
                  100:"C",
                  400:"CD",
                  500:"D",
                  900:"CM",
                  1000:"M"}
    result = []
    if number <= 0 or number > 3999:
        raise ValueError("Invalid input number")

    while number > 0:

        #find the closet number in dict for given number
        max_key = 1
        for key in sorted(roman_dict.iterkeys(), reverse=True):
            if key < number:
                max_key = key
                break
            elif key == number:
                max_key = key
                break
            else:
                max_key = key
                continue

        if number >= max_key:
            div = number/max_key
            for i in range(div):
                result.append(roman_dict[max_key])

            number = number%max_key

    return "".join(result)

if __name__ == '__main__':
    int_number = 1
    print "int number : " + str(int_number) + " roman value: ",
    print intToRoman(int_number)

    int_number = 4
    print "int number : " + str(int_number) + " roman value: ",
    print intToRoman(int_number)

    int_number = 8
    print "int number : " + str(int_number) + " roman value: ",
    print intToRoman(int_number)

    int_number = 9
    print "int number : " + str(int_number) + " roman value: ",
    print intToRoman(int_number)

    int_number = 19
    print "int number : " + str(int_number) + " roman value: ",
    print intToRoman(int_number)

    int_number = 14
    print "int number : " + str(int_number) + " roman value: ",
    print intToRoman(int_number)

    int_number = 15
    print "int number : " + str(int_number) + " roman value: ",
    print intToRoman(int_number)

    int_number = 141
    print "int number : " + str(int_number) + " roman value: ",
    print intToRoman(int_number)

    int_number = 200
    print "int number : " + str(int_number) + " roman value: ",
    print intToRoman(int_number)

    int_number = 400
    print "int number : " + str(int_number) + " roman value: ",
    print intToRoman(int_number)

    int_number = 900
    print "int number : " + str(int_number) + " roman value: ",
    print intToRoman(int_number)

    int_number = 1449
    print "int number : " + str(int_number) + " roman value: ",
    print intToRoman(int_number)

    int_number = 3549
    print "int number : " + str(int_number) + " roman value: ",
    print intToRoman(int_number)