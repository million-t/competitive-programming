# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        cum_sum = 0
        def dfs(node):
            nonlocal cum_sum
            
            if node.right:
                dfs(node.right)
            
            
            cum_sum += node.val
            node.val = cum_sum
            
            if node.left:
                dfs(node.left)
            
            
            
            
    
        
        dfs(root)
        return root