import sys
class Solution(object):

    #python doesn't support inplace sorting hence implemented the same.
    #another approach would be to use numpy library
    # import numpy as np
    # a = np.array([4, 8, 1, 7, 3, 0, 5, 2, 6, 9])
    # a[1:4].sort()
    def sort_in_place(self, nums, idx):
        for i in range(idx, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] < nums[i]:
                    nums[j],nums[i] = nums[i], nums[j]


    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # loop through sequence from right
        # till you find where nxt number is lower than current.
        # if not found such a situation, print sorted list
        # else find the next number from before the list and swap it with b, then sort the list from a
        i = len(nums) - 1
        while i >= 1:
            if nums[i] > nums[i-1]:
                break;
            i -= 1
        if i <= 0:
            self.sort_in_place(nums, 0)
        else:
            a = nums[i-1]
            b = nums[i]
            j = i+1
            minn = b-a
            j_minn = i

            while j < len(nums):
                if nums[j] > a and nums[j] - a <= minn:
                    j_minn = j
                    minn = nums[j]
                j += 1

            print i-1,i,j,minn
            #swap
            nums[i-1], nums[j_minn] = nums[j_minn], nums[i-1]

            print nums
            #sort nums after i
            self.sort_in_place(nums,i)
            print nums
            # print nums2
            # return nums


