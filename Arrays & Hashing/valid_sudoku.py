class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grid=[[set() for _ in range(0,3)] for _ in range(0,3)]
        rows=[set() for _ in range(0,9)]
        cols=[set() for _ in range(0,9)]
        
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j].isnumeric():
                    x=i//3
                    y=j//3
                    num=board[i][j]
                    
                    if (num in rows[i]) or (num in cols[j]) or (num in grid[x][y]):
                        return False
                    else:
                        rows[i].add(num)
                        cols[j].add(num)
                        grid[x][y].add(num)
        return True