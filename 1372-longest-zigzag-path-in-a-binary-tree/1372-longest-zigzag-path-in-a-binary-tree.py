# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        def dfs(node):
            nonlocal ans
            
            if not node:
                return -1, -1
            
            left_l, left_r = dfs(node.left)
            right_l, right_r = dfs(node.right)
            cur_l = left_r + 1
            cur_r = right_l + 1
            ans = max(ans, cur_l, cur_r)
            return cur_l, cur_r
        
        dfs(root)
        return ans
            
            
            
            
        