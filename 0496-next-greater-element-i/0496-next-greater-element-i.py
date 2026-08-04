class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack=[]
        ans=[]
        next={}
        n=len(nums1)
        m=len(nums2)
        for i in range(m-1,-1,-1):
            current=nums2[i]
            while stack and stack[-1]<current:
                stack.pop()
            if not stack:
                next[current]=-1
            else:
                next[current]=stack[-1]
            stack.append(current)
        for num in nums1:
            ans.append(next[num])
        return ans


        