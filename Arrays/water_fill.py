# how much water can be filled between buildings or in dips or combination of dips and buildings.
# negative array element indicates deeps, 0 indicates flat surface.

def water_fill(nums):

    if not nums:
        return 0

    left = [0 for x in range(len(nums))]
    right = [0 for x in range(len(nums))]

    left[0] = nums[0]

    for i in range(1, len(nums)):
        left[i] =  max(left[i-1], nums[i])

    right[len(nums)-1] = nums[len(nums)-1]
    for i in range(len(nums)-2, -1, -1):
        right[i] = max(right[i+1], nums[i])

    water = 0
    print left
    print right
    for i in range(len(nums)):
        minn = min(left[i],right[i])
        if minn < 0 and nums[i] < 0:
            water += nums[i] * -1
        else:
            water += (minn - nums[i])

    return water

nums = []
print nums,
print "water: ",
print str(water_fill(nums))

nums = [4,1,4]
print nums,
print "water: ",
print str(water_fill(nums))

nums = [4,5,4]
print nums,
print "water: ",
print str(water_fill(nums))

nums = [5,2,3,6]
print nums,
print "water: ",
print str(water_fill(nums))

nums = [1,2,3,4,5]
print nums,
print "water: ",
print str(water_fill(nums))

nums = [5,4,3,2,1]
print nums,
print "water: ",
print str(water_fill(nums))

nums = [5,5,5,5]
print nums,
print "water: ",
print str(water_fill(nums))

nums = [5,4,5,2,3,6]
print nums,
print "water: ",
print str(water_fill(nums))

#insteade of buidling it might be dips too.
nums = [5,-4,5,2,3,6]
print nums,
print "water: ",
print str(water_fill(nums))

#insteade of buidling it might be dips too.
nums = [5,-4,5,2,3,6]
print nums,
print "water: ",
print str(water_fill(nums))

#having first and last as dips
nums = [-5,-4,5,2,3,6]
print nums,
print "water: ",
print str(water_fill(nums))

nums = [0,-4,5,2,3,0]
print nums,
print "water: ",
print str(water_fill(nums))

#all dips
nums = [-4,-5,-2,-3]
print nums,
print "water: ",
print str(water_fill(nums))


