# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        
        def topDown(node):
            if not node:
                return 0, 0
            
            
            left_prev1, left_prev2 = topDown(node.left)
            right_prev1, right_prev2 = topDown(node.right)
            
            cand1 = left_prev1 + right_prev1
            cand2 = left_prev2 + right_prev2 + node.val
            
            return max(cand1, cand2), cand1
        
        return topDown(root)[0]