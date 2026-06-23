class Solution(object):
    def moveZeroes(self, nums):
        j=0
        size=len(nums)
        for i in range(size):
            if nums[i]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
        return nums

        
        