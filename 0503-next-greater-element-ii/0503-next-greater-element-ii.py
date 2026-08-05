class Solution(object):
    def nextGreaterElements(self, nums):
        n=len(nums)
        stack=[]
        res=[-1]*n
        for i in range(2*n-1,-1,-1):
            current=nums[i%n]
            while stack and stack[-1]<=current:
                stack.pop()
            if i<n:
                if stack:
                    res[i]=stack[-1]
            stack.append(current)
        return res
        