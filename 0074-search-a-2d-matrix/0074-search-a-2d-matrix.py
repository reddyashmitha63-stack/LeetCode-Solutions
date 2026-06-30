class Solution(object):
    def searchMatrix(self, matrix, target):
        n=len(matrix)
        m=len(matrix[0])
        left=0
        right=n*m-1
        while left<=right:
            mid=(left+right)//2
            row=mid//m
            column=mid%m
            if matrix[row][column]==target:
                return True
            elif matrix[row][column]>target:
                right=mid-1
            else:
                left=mid+1
        return False
