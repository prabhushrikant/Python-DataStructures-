import bisect
import itertools

def binarySearch(nums, key):
    # return bisect.bisect(nums, key)
    search_res = bisect.bisect(nums,key)
    if nums and nums[search_res-1]==key:
        return True
    else:
        return False

    # if search_res <= 0 or search_res >= len(nums):
    #     return False
    # else:
    #     if nums[search_res - 1] == key:
    #         return True
    #     else:
    #         return False
    # return False if bisect.bisect(nums, key) >= len(nums) else True

def search_in_sorted_matrix(matrix, key):
    flat_list = list(itertools.chain.from_iterable(matrix))
    # flat_list = list(itertools.chain(*matrix))
    print flat_list
    return binarySearch(flat_list, key)

nums = [1,2,3,4,8,15]
key = 3
print str(binarySearch(nums, key))

nums = [1]
key = 1
print str(binarySearch(nums, key))

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
key = 16
print search_in_sorted_matrix(matrix, key)
# for row in matrix:
#     print row

