
# this solution is good for repeated as well as non repeating numbers in the list.
# time complexity average case O(lg(n)) , worst case O(n)

# Note: all these while loops are required for skipping the same numbers, because it's not changing condition

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r)/2
            if nums[mid] == target:
                return mid
            else:
                #check which way to go , because array is shifted , we don't know which half is higher than mid and which is
                # lower, we can look the starting points of each half and see if our target can be found there, if yes we move in
                # that direction
                if nums[l] < nums[mid]:
                    #left array is sorted.
                    #check if target can be found in left array.
                    #Note : this condition can be written only for sorted arrays, hence is the check sorted array before.
                    if nums[l] <= target and nums[mid] >= target:
                        r = mid-1
                        while l <= r and r < len(nums)-1 and nums[r] == nums[r+1]: r -= 1
                    else:
                        #required in case when number are repeated e.g. [1, 3, 1, 1, 1]
                        l = mid + 1
                        while l <= r and l > 0 and nums[l-1] == nums[l]: l += 1
                elif nums[l] == nums[mid]:
                    # in this cases, may be left half and right half
                    l += 1 #<= this is required, as default to make outer while loop exit if in case following while loop condition doesn't hold true.
                    while l <= r and l > 0 and nums[l-1] == nums[l]: l += 1
                else:
                    #right array should be sorted,
                    #check if target can be found in right array.
                    if nums[mid] <= target and nums[r] >= target:
                        l = mid+1
                        while l <= r and l > 0 and nums[l-1] == nums[l]: l += 1
                    else:
                        r = mid - 1
                        while l <= r and r < len(nums)-1 and nums[r] == nums[r+1]: r -= 1

        return -1

#driver program

sol = Solution()
# l = [6,7,1,2,3,4,5]
# t = 6
# print str(sol.search(l,t))
#
# l = [5,1,3]
# t = 5
# print str(sol.search(l,t))
#
# l = [1,3]
# t = 3
# print str(sol.search(l,t))
#
# l = [4,5,6,7,0,1,2]
# t = 0
# print str(sol.search(l,t))
#
# l = [4,5,6,7,0,1,2]
# t = 3
# print str(sol.search(l,t))
#
l = [1,3,1,1,1]
t = 3
print str(sol.search(l,t))
#
# l = [4,4,1,2,3]
# t = 4
# print str(sol.search(l,t))
#
# l = [1,3]
# t = 1
# print str(sol.search(l,t))

# l = [1,2,1]
# t = 0
# print str(sol.search(l,t))

l = [1,1,3,1]
t = 3
print str(sol.search(l,t))