"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited={}
        dequeue=deque()
        
        dequeue.append(node)
        visited[node]=Node(node.val)
        
        while dequeue:
            level=dequeue.popleft()
            for neighbor in level.neighbors:
                if neighbor not in visited:
                    dequeue.append(neighbor)
                    visited[neighbor]=Node(neighbor.val)
                visited[level].neighbors.append(visited[neighbor])
        return visited[node]