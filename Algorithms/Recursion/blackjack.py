def handValue(l, index, sum):
    if len(l) == index:
        return sum
    else:
        if l[index] == 'A':
            if sum + 11 <= 21:
                sum1 = handValue(l, index+1, sum+1)
                sum2 = handValue(l, index+1, sum+11)
                if sum1 > 21:
                    if sum2 > 21:
                        return min(sum1, sum2)
                    else:
                        return sum2
                else:
                    if sum2 > 21:
                        return sum1
                    else:
                        return max(sum1, sum2)
            else:
                return handValue(l, index+1, sum+1)
        else:
            if l[index] in ['K','Q','J']:
                return handValue(l, index+1, sum+10)
            else:
                return handValue(l, index+1, sum+int(l[index]))


if __name__ == "__main__":

    hands = [["4","5","J"],  #19
             ["2","Q","J"],  #22
             ["A","A","K"],  #12
             ["5","4","A","A", "A"],  #?
            ]
    for l in hands:
        print "Hand : ",
        print l,
        print "Value : " + str(handValue(l, 0, 0))
