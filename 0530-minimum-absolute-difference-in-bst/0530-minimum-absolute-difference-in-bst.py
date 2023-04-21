# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        MINDIF = float('inf')
        
        def dfs(node):
            nonlocal MINDIF
            
            if not node:
                return float('inf'), float('-inf')
            
            leftMin, leftMax = dfs(node.left)
            rightMin, rightMax = dfs(node.right)
            
            MINDIF = min(MINDIF, min(abs(leftMax - node.val), abs(rightMin - node.val)))
            
            return min(leftMin, node.val), max(rightMax, node.val)
        
        dfs(root)
        
        return MINDIF
            