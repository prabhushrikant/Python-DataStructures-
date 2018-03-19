#program to get median of median using functional programming and immutable objects.

def median(rcvd_tuple):
    l = len(rcvd_tuple)
    if l % 2 == 0:
        m = (rcvd_tuple[l/2 - 1] + rcvd_tuple[l/2])/2.0
    else:
        m = rcvd_tuple[l/2]
    return m

if __name__ == '__main__':
    line1 = [4234, 22, 123, 234, 3322, 32, 2, 444]
    line2 = [42,2212, 1224, 22]
    line3 = [3234, 44, 1, 2, 1, 233, 1234]
    fset1 = tuple(sorted(line1))
    fset2 = tuple(sorted(line2))
    fset3 = tuple(sorted(line3))

    print median(tuple(sorted([median(fset1), median(fset2), median(fset3)])))
