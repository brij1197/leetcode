# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def height(node,value,h):
            if not node: return 0
            if node.val==value: return h
            left_height=height(node.left,value,h+1)
            if left_height: return left_height
            right_height=height(node.right,value,h+1)
            if right_height: return right_height
            
        def find_parent(node,value):
            if not node: return
            if (node.left and node.left.val==value) or (node.right and node.right.val==value): return node.val
            left_parent=find_parent(node.left,value)
            if left_parent: return left_parent
            return find_parent(node.right,value)
        x_height,x_parent=height(root,x,0),find_parent(root,x)
        y_height,y_parent=height(root,y,0),find_parent(root,y)
        
        if x_height==y_height and x_parent!=y_parent:
            return True
        return False