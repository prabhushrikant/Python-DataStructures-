def binary_search(arr2 , l , r, t):
    # print "searching "+ str(t)
    if l > r or l < 0:
        return False
    else:
        mid = (l + r)/2
        if arr2[mid] == t:
            return True
        else:
            if t < arr2[mid]:
                binary_search(arr2, l, mid-1, t)
            else:
                binary_search(arr2, mid+1, r, t)

        #return False # this could be the problem

def find_duplicates(arr1, arr2):
    result = []
    i = 0
    arr = arr1 if len(arr1) <= len(arr2) else arr2
    print arr

    barr = arr2 if len(arr1) < len(arr2) else arr1
    print barr

    for i in range(len(arr)):
        if binary_search(barr,0,len(barr)-1,arr[i]):
            result.append(arr[i])
    return result

if __name__ == '__main__':
    arr1=[1,2,3,5,6,7]
    arr2=[3,6,7,8,20]

    print find_duplicates(arr1, arr2)
