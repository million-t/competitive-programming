# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        
        self.ans = 0
        def dfs(node):
            
            if not node: return 0, 0
            
            left_neg, left_pos = dfs(node.left)
            right_neg, right_pos = dfs(node.right)
            
            neg = left_neg + right_neg
            pos = right_pos + left_pos
            temp = pos - neg + node.val - 1
            self.ans += temp
            
            return min(0, pos + neg + node.val - 1), max(0, pos + neg + node.val - 1)
        
        dfs(root)
        return self.ans
        
        
        