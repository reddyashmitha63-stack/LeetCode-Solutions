class Solution(object):
    def findPeakGrid(self, mat):
        n=len(mat)
        m=len(mat[0])
        top=0
        bottom=n-1
        while top<=bottom:
            mid=(top+bottom)//2
            max_col=0
            for j in range(m):
                if mat[mid][j]>mat[mid][max_col]:
                    max_col=j
            up = -1 if mid == 0 else mat[mid-1][max_col]
            down = -1 if mid == n-1 else mat[mid+1][max_col]
            if mat[mid][max_col] > up and mat[mid][max_col] > down:
                return [mid, max_col]
            elif up > mat[mid][max_col]:
                bottom = mid - 1
            else:
                top = mid + 1
        return [-1,-1]
            
                    