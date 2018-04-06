# Write a program to make change of amount M with infinite number of
# {quarters, dimes, nickels and cents}

def makeChange(sum, q, d, n, c, M, cache):
    key = ",".join([str(q),str(d),str(n),str(c),str(sum)])
    if sum > M:
        return
    elif sum == M:
        if key not in cache:
            print "{} quarters, {} dimes, {} nickels and {} cents".format(q,d,n,c)
            cache[key] = True #mark this combination as seen.
        else:
            return
    elif key in cache:
        return
    else:
        makeChange(sum+25, q+1, d, n, c, M, cache)
        makeChange(sum+10, q, d+1, n, c, M, cache)
        makeChange(sum+5, q, d, n+1, c, M,  cache)
        makeChange(sum+1, q, d, n, c+1, M,  cache)

if __name__ == "__main__":
    M = int(raw_input().strip())
    if M < 0:
        print "Invalid amount specified."
    else:
        cache = {} #map containing key (format: [q,d,n,c,sum]) to check if prog has seen it before
        makeChange(0,0,0,0,0,M,cache)