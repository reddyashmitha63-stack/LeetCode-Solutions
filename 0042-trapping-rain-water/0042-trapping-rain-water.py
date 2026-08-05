class Solution(object):
    def trap(self, height):
        n=len(height)
        if height is None:
            return 0
        leftMax=[]
        rightMax=[]
        left_maxi=height[0]
        right_maxi=height[n-1]
        total_water=0
        for i in range(n):
            left_maxi=max(height[i],left_maxi)
            leftMax.append(left_maxi)
        for i in range(n-1,-1,-1):
            right_maxi=max(height[i],right_maxi)
            rightMax.append(right_maxi)
        rightMax.reverse()
        for i in range(n):
            water_level=min(leftMax[i],rightMax[i])
            water=water_level-height[i]
            total_water+=water
        return total_water



        