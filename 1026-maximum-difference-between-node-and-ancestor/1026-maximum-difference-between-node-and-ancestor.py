# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        def dfs(node, _min, _max):
            nonlocal ans
            
            if not node:
                return
            
            ans = max(ans, abs(node.val - _min), abs(node.val - _max))
            
            dfs(node.left, min(node.val, _min), max(node.val, _max))
            dfs(node.right, min(node.val, _min), max(node.val, _max))
        
        dfs(root, root.val, root.val)
        
        return ans