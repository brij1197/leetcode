class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows,columns=len(matrix),len(matrix[0])
        
        row_min=float('-inf')
        for row in range(rows):
            row_min=max(min(matrix[row]),row_min)

        col_max=float('inf')
        for col in range(columns):
            col_max=min(max(matrix[row][col] for row in range(rows)),col_max)
            
        return [row_min] if row_min==col_max else []