# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        queue=collections.deque()
        for num in nums:
            node=TreeNode(num)
            
            while queue and num>queue[-1].val:
                node.left=queue.pop()
                
            if queue:
                queue[-1].right=node
            
            queue.append(node)
        return queue[0]