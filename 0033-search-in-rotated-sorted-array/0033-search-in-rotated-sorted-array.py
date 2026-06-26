class Solution(object):
    def search(self, nums, target):
        size=len(nums)
        left=0
        right=size-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>=nums[left]:
                if nums[left]<=target and target<=nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            elif nums[mid]<=nums[right]:
                if nums[mid]<=target and target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return -1
        