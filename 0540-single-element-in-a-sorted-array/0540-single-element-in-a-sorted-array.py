class Solution(object):
    def singleNonDuplicate(self, nums):
        size=len(nums)
        left=0
        right=size-1
        while left<=right:
            mid=(left+right)//2
            if mid==0 or mid==size-1:
                return nums[mid]
            elif nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1]:
                return nums[mid]
            elif mid%2==0 and nums[mid]==nums[mid+1]:
                left=mid+2
            elif mid%2!=0 and nums[mid]==nums[mid-1]:
                left=mid+1
            else:
                right=mid-1

        
       
        