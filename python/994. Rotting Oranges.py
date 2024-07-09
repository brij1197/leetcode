from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited=set()
        current=deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j]==1):
                    visited.add((i,j))
                elif (grid[i][j]==2):
                    current.append((i,j))
        result=0
        while visited and current:
            for _ in range(len(current)):
                i,j=current.popleft()
                for coordinate in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                    if coordinate in visited:
                        visited.remove(coordinate)
                        current.append(coordinate)
            result+=1
        return -1 if visited else result