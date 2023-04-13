# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_sum = float('-inf')
        
        def dfs(node):
            nonlocal max_sum
            
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            cur = node.val
    
            max_sum = max(max_sum, max(left, 0) + max(right, 0) + cur)
            
            return max(left + cur, right + cur, cur)
            
            
        dfs(root)
        
        return max_sum        
        