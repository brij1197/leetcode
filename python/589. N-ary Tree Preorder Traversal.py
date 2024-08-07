"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output=[]
        def traverse(root,output):
            if not root: return
            output.append(root.val)
            for child in root.children:
                traverse(child,output)
        traverse(root,output)
        return output