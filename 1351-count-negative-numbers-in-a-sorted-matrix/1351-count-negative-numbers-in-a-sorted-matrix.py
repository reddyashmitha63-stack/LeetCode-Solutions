class Solution(object):
    def countNegatives(self,grid):
        m,n=len(grid),len(grid[0])
        count=0
        for row in grid:
            left,right=0,n-1
            first_neg=n 
            while left<=right:
                mid=(left+right)//2
                if(row[mid]<0):
                    first_neg=mid
                    right=mid-1 
                else:
                    left=mid+1 
            count=count+(n-first_neg)
        return count
       