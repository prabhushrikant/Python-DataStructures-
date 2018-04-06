def find_first_set_bit(n):

    count = 1
    c = n
    while c != 0:
        if c & 1 == 1:
            break;
        count += 1
        c = c >> 1
    return count

if __name__ == '__main__':
    print "first set bit (counted from right) : " + str(find_first_set_bit(18))

