class Solution(object):
    def findNSE(self, arr):
        n=len(arr)
        ans=[0]*n
        st=[]
        for i in range(n-1,-1,-1):
            current=arr[i]
            while st and arr[st[-1]]>=arr[i]:
                st.pop()
            if st:
                ans[i]=st[-1]
            else:
                ans[i]=n
            st.append(i)
        return ans
    def findPSE(self,arr):
        n=len(arr)
        st=[]
        ans=[0]*n
        for i in range(n):
            current=arr[i]
            while st and arr[st[-1]]>arr[i]:
                st.pop()
            if st:
                ans[i]=st[-1]
            else:
                ans[i]=-1
            st.append(i)
        return ans
    def sumSubarrayMins(self, arr):
        n=len(arr)
        nse = self.findNSE(arr)
        pse = self.findPSE(arr)
        mod = 10**9 + 7
        total_sum = 0
        for i in range(n):
            left=i-pse[i]
            right=nse[i]-i
            freq=left*right
            total_sum+=arr[i]*freq
            total_sum%=mod
        return total_sum
        
        
        