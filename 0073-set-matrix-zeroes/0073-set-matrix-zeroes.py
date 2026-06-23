class Solution(object):
    def setZeroes(self, matrix):
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    for col in range(n):
                        if matrix[i][col]!=0:
                            matrix[i][col]="x"
                    for row in range(m):
                        if matrix[row][j]!=0:
                            matrix[row][j]="x"
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="x":
                    matrix[i][j]=0
        return matrix