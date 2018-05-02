#not completely working solution., prints the correctly formed array but result is false.
def countArrayRec(n, k, i, j, l, r, res):
    if i+1 >= j:
        print res
        return 1
    else:
        result = 1
        res2 = list(res)
        for p in range(1,k+1):
            if p != l:
                if i + 2 == j:
                    if p != r:
                        res2[i+1] = p
                        result = 1 + countArrayRec(n, k, i+1, j, p, r, res2)
                else:
                    res2[i+1] = p
                    result = 1 + countArrayRec(n, k, i+1, j, p, r, res2)
        return result

def countArray(n, k, x):
    # Return the number of ways to fill in the array.
    if k < n-2:
        return 0
    else:
        res = [-1 for i in range(n)]
        res[0] = 1
        res[n-1] = x
        print res
        return countArrayRec(n,k,0,n-1,1,x,res)


n = 5
k = 3
x = 2
print countArray(n,k,x)