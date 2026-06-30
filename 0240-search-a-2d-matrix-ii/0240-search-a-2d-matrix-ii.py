class Solution(object):
    def searchMatrix(self, matrix, target):
        top=0
        bottom=len(matrix)-1
        left=0
        right=len(matrix[0])-1
        while top<len(matrix) and right>=0:
            if matrix[top][right]==target:
                return True
            elif matrix[top][right]>target:
                right-=1
            else:
                top+=1
        return False


        