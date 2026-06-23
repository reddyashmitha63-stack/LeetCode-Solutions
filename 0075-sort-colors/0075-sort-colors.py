class Solution(object):
    def sortColors(self, nums):
        size=len(nums)
        for i in range(size):
            for j in range(size-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums