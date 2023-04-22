# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        
        def dfs(node):
            if not node:
                return True
            
            left = dfs(node.left)
            
            if not left:
                return False
            
            right = dfs(node.right)
            
            if not right:
                return False
            
            if abs(left - right) > 1:
                return False
            
            return max(left, right) + 1
        
        return dfs(root)
        