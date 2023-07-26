# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        ans = 0 
        def dfs(node, left, zigzag):
            nonlocal ans
            ans = max(zigzag, ans)
            
            if not node:
                return
            
            if left:
                dfs(node.left, left, 0)
                dfs(node.right, not left, zigzag + 1)
            
            else:
                dfs(node.left, not left, zigzag + 1)
                dfs(node.right, left, 0)
        
        dfs(root.left, True, 0)
        dfs(root.right, False, 0)
        return ans
                
            
            
        