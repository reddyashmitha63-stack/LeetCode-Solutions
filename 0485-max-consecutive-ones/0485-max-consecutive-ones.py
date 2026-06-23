class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        size=len(nums)
        count=0
        maxi=0
        for i in range(size):
            if nums[i]==1:
                count+=1
            else:
                count=0
            maxi=max(maxi,count)
        return maxi
        