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

def find_grants_cap_1(grantsArray, newBudget):

    #first imagine all the people are affected.
    no_affected = len(grantsArray)

    curr_budget = 0
    surplus = 0
    avg = (newBudget - surplus)/no_affected

    while curr_budget < newBudget:
        curr_budget = 0
        no_affected = len(grantsArray)
        surplus = 0
        for grant in grantsArray:
            if grant < avg:
                no_affected += -1
                surplus += grant
                curr_budget += grant
            else:
                curr_budget += avg
        avg = (newBudget - surplus)/no_affected

    if curr_budget == newBudget:
        return avg
    else:
        return -1

def award_cut():
    # import java.io.*;
    # import java.util.*;
    #
    # class Solution {
    #
    # static double findGrantsCap(double[] grantsArray, double newBudget) {
    # // your code goes here
    # if (grantsArray == null || grantsArray.length == 0 || newBudget < 0)
    # {
    # return -1;
    # }
    # int noImpacted = grantsArray.length;
    # double cap = newBudget/noImpacted;
    # while (noImpacted > 0 && cap*noImpacted + over <= newBudget)
    #     {
    #         double leftover = 0;
    # double over =0;
    # for (int i=0;i<grantsArray.length;i++)
    # {
    # if (grantsArray[i] <= cap)
    # {
    # leftover = leftover + grantsArray[i] - cap;
    # noImpacted--;
    # }
    # else
    # {
    # over = over + grantsArray[i];
    # }
    # }
    # cap = cap + leftover/noImpacted;
    # }
    # return cap;
    pass

if __name__ == '__main__':
    grants = [2, 100, 50, 120, 1000]
    new_budget = 190
    print str(find_grants_cap_1(grants, new_budget))

    grants = [2, 100, 50, 120, 167]
    new_budget = 400
    print str(find_grants_cap_1(grants, new_budget))

    grants = [2, 100, 50, 132, 167]
    new_budget = 400
    print str(find_grants_cap_1(grants, new_budget))

    grants = [210,200,150,193,130,110,209,342,117]
    new_budget = 1530
    print str(find_grants_cap(grants, new_budget))