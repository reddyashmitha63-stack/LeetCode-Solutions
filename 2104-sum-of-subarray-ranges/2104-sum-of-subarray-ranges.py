class Solution(object):
    def getMin(self,nums):
        n=len(nums)
        pse=[-1]*n
        nse=[n]*n
        st=[]
        for i in range(n):
            while st and nums[st[-1]]>=nums[i]:
                st.pop()
            if st:
                pse[i]=st[-1]
            st.append(i)
        st=[]
        for i in range(n-1,-1,-1):
            while st and nums[st[-1]]>nums[i]:
                st.pop()
            if st:
                nse[i]=st[-1]
            st.append(i)
        maxi=0
        for i in range(n):
            left=i-pse[i]
            right=nse[i]-i
            freq=left*right
            maxi+=nums[i]*freq
        return maxi
    def getMax(self,nums):
        n=len(nums)
        pge=[-1]*n
        nge=[n]*n
        st=[]
        for i in range(n):
            while st and nums[st[-1]]<=nums[i]:
                st.pop()
            if st:
                pge[i]=st[-1]
            st.append(i)
        st=[]
        for i in range(n-1,-1,-1):
            while st and nums[st[-1]]<nums[i]:
                st.pop()
            if st:
                nge[i]=st[-1]
            st.append(i)
        mini=0
        for i in range(n):
            left=i-pge[i]
            right=nge[i]-i
            freq=left*right
            mini+=nums[i]*freq
        return mini 


    def subArrayRanges(self, nums):
        minSum = self.getMin(nums)
        maxSum = self.getMax(nums)

        return maxSum - minSum
        