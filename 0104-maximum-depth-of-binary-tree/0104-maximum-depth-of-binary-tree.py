# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left) + 1
        right_depth = self.maxDepth(root.right) + 1
        
        return max(left_depth, right_depth)
        
        
        
        
#         if not root: 
#             return level
        
#         return max(self.maxDepth(root.left, level + 1), self.maxDepth(root.right, level + 1))