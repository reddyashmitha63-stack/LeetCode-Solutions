class Solution(object):
    def removeDuplicates(self, nums):
        size=len(nums)
        l=[]
        for i in range(size):
            if nums[i] not in l:
                l.append(nums[i])
        for i in range(len(l)):
            nums[i]=l[i]
        return len(l)
        