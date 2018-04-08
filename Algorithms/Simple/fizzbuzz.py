for i in range(100):
    if i%3 == 0 or i%5 == 0:
        if i%3 == 0:
            print "fizz ",
        if i%5 == 0:
            print "bizz ",
    else:
        print str(i) + " ",