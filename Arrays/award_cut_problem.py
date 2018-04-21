def find_grants_cap(grantsArray, newBudget):

    avg_grant = newBudget/float(len(grantsArray))

    amount_dist = 0
    count_less = 0
    for i in range(len(grantsArray)):
        if grantsArray[i] < avg_grant:
            amount_dist += avg_grant - grantsArray[i]
            count_less += 1

    dist_btw = len(grantsArray) - count_less
    l = []


    for i in range(len(grantsArray)):
        # print "distributed btw : " + str(dist_btw)
        new_grant = avg_grant + amount_dist/float(dist_btw)
        if grantsArray[i] > avg_grant and new_grant > grantsArray[i] and dist_btw > 0:
            dist_btw -= 1
        else:
            if grantsArray[i] > avg_grant:
                l.append(i) #elements which need adjustments in grants

    # print l
    sum1 = 0
    max_element = 0
    for i in range(len(grantsArray)):
        if grantsArray[i] > max_element:
            max_element = grantsArray[i]
        if i not in l:
            sum1 += grantsArray[i]

    cap_final = 0
    # print sum1
    if len(l) == 0:
        cap_final = new_budget - (sum1 - max_element)
    else:
        cap_final = (newBudget - sum1)/float(len(l))
    # print cap_final
    return cap_final


if __name__ == '__main__':
    grants = [2, 100, 50, 120, 167]
    new_budget = 400
    print str(find_grants_cap(grants, new_budget))

    grants = [210,200,150,193,130,110,209,342,117]
    new_budget = 1530
    print str(find_grants_cap(grants, new_budget))