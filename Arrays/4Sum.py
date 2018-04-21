class Solution(object):

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = set()
        nums = sorted(nums)
        print nums

        for i in range(len(nums)-3):
            sum1 = nums[i]
            # print sum1
            t = target - sum1
            l = i + 1
            r = len(nums)-1
            if i == 0 or nums[i] != nums[i-1]:
                while l < r:
                    sum2 = nums[l] + nums[r]
                    t2 = t - sum2
                    l1 = l
                    r1 = r
                    while l1 < r1:
                        if nums[l1] == t2 and l1 != l:
                            res.add(tuple(sorted([nums[i], nums[l], nums[r], nums[l1]])))
                            while l1 < r1 and nums[l1] == nums[l1+1]: l1 += 1
                            while l1 < r1 and nums[r1] == nums[r1-1]: r1 -= 1
                            l1 += 1
                            r1 -= 1
                        elif nums[r1] == t2 and r1 != r:
                            res.add(tuple(sorted([nums[i], nums[l], nums[r], nums[r1]])))
                            while l1 < r1 and nums[l1] == nums[l1+1]: l1 += 1
                            while l1 < r1 and nums[r1] == nums[r1-1]: r1 -= 1
                            r1 -= 1
                            l1 += 1
                        else:
                            if nums[l1] <= t2:
                                l1 += 1
                            else:
                                r1 -= 1
                    if sum2 <= t:
                        l += 1
                    else:
                        r -= 1

        result = []
        for s in res:
            result.append(s)
        return sorted(result)


if __name__ == '__main__':

    nums = [-3,-1,0,2,4,5]
    target = 2
    sol = Solution()
    print sol.fourSum(nums, target)
