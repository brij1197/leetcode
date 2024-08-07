# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        hashmap={val:idx for idx,val in enumerate(inorder)}
        preorder=deque(preorder)
        def build(inStart,inEnd):
            if inStart>inEnd or not preorder:
                return None
            root=TreeNode(preorder.popleft())
            root.left=build(inStart,hashmap[root.val]-1)
            root.right=build(hashmap[root.val]+1,inEnd)
            return root
        return build(0,len(inorder)-1)