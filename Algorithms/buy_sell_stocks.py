# https://practice.geeksforgeeks.org/problems/stock-buy-and-sell/0

def maxProfit(days):
    b_index = 0
    s_index = b_index
    profit = 0

    i = 0
    while i < len(days):
        # print "day: "+ str(i)
        if days[b_index] <= days[i] and days[i]-days[b_index] > profit:
            s_index = i
            profit = days[i]-days[b_index]
            # print "Profit: " + str(profit)
        else:
            if profit > 0:
                print("("+str(b_index)+" "+str(s_index)+"), "),
                profit = 0
            b_index = i
            s_index = b_index
        i += 1

    if profit > 0:
        print("("+str(b_index)+", "+str(s_index)+"), "),


if __name__ == '__main__':

    # days = [100, 180, 260, 310, 40, 535, 695]
    days = [100, 40, 20, 60, 90, 15, 300]
    # days = [23, 13, 25, 29, 33, 19, 34, 45, 65, 67]

    maxProfit(days)