class Solution(object):
    def minEatingSpeed(self, piles, h):
        n=len(piles)
        left=1
        right=max(piles)
        while left<=right:
            mid=(left+right)//2
            hours=0
            for i in range(n):
                hours+=(piles[i]+mid-1)//mid
            if hours<=h:
                right=mid-1 
            else:
                left=mid+1
        return left

        