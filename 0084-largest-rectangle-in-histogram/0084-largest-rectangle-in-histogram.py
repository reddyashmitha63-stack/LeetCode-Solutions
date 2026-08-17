class Solution(object):
    def findNSE(self,heights):
        n=len(heights)
        ans=[0]*n
        st=[]
        for i in range(n-1,-1,-1):
            current=heights[i]
            while st and heights[st[-1]]>=heights[i]:
                st.pop()
            if st:
                ans[i]=st[-1]
            else:
                ans[i]=n
            st.append(i)
        return ans
    def findPSE(self,heights):
        n=len(heights)
        ans=[0]*n
        st=[]
        for i in range(n):
            current=heights[i]
            while st and heights[st[-1]]>heights[i]:
                st.pop()
            if st:
                ans[i]=st[-1]
            else:
                ans[i]=-1
            st.append(i)
        return ans
    def largestRectangleArea(self, heights):
        n=len(heights)
        nse = self.findNSE(heights)
        pse = self.findPSE(heights)
        maxi=0
        for i in range(n):
            width=nse[i]-pse[i]-1
            area=heights[i]*width
            maxi=max(area,maxi)
        return maxi