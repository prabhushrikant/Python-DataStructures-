def hex_to_decimal(hex_str):
    hex_digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    hex_str = hex_str.upper()
    power = len(hex_str)-1
    val = 0
    for c in hex_str:
        index = hex_digits.index(c)
        val += index * (16**power)
        power -= 1
    return val


if __name__ == "__main__":
    print "enter hex number: ",
    hex_str = raw_input().strip()
    print
    print "decimal number: ",
    dec_number = hex_to_decimal(hex_str)
    print dec_number,
    print