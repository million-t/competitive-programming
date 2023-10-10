# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.ans = True
        def dfs(node):
            if not self.ans:
                return 0, 0
                
            
            if not node:
                return float('inf'), float('-inf')
            
            left_min, left_max = dfs(node.left)
            right_min, right_max = dfs(node.right)
            
            if not left_max <  node.val < right_min:
                self.ans = False
                return 0, 0
            
            return min(left_min, node.val), max(node.val, right_max)
        
        
        dfs(root)
        return self.ans
        