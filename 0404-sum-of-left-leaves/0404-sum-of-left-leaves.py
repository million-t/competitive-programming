# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(node, left = False):
            
            if not (node.left or node.right):
                _sum = node.val if left else 0
                return _sum
            
            _sum = 0
            if node.left:
                _sum +=  dfs(node.left, True)
            
            if node.right:
                _sum +=  dfs(node.right, False)
            
            return _sum
        
        return dfs(root)