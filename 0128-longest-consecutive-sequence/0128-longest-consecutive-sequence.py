class Solution(object):
    def longestConsecutive(self, nums):
        size=len(nums)
        if size==0:
            return 0
        nums.sort()
        count=1
        maxi=1
        for i in range(size-1):
            if nums[i+1]-nums[i]==1:
                count+=1
            elif nums[i+1]==nums[i]:
                continue
            else:
                count=1
            maxi=max(count,maxi)
    
        return maxi

        
        