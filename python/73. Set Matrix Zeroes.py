class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        
        rows,cols=[],[]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    rows.append(i)
                    cols.append(j)
                    
        for row in rows:
            for j in range(n):
                matrix[row][j]=0
        
        for i in range(m):
            for col in cols:
                matrix[i][col]=0