class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for _ in range(0,9)]
        column=[set() for _ in range(0,9)]
        grid=[[set() for _ in range(0,3)] for _ in range(0,3)]
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j].isnumeric():
                    x=j//3
                    y=i//3
                    num=board[i][j]
                    
                    if (num in grid[x][y]) or (num in row[i]) or (num in column[j]):
                        return False
                    else:
                        row[i].add(num)
                        column[j].add(num)
                        grid[x][y].add(num)
        return True