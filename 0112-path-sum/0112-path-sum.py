# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, path_sum, targetSum):
            
            
            if not node:
                return False
            
            path_sum += node.val
            if not (node.left or node.right):
                return path_sum == targetSum
            
            
            left = dfs(node.left, path_sum, targetSum)
            
            if left:
                return left
            
            right = dfs(node.right, path_sum, targetSum)
            
            return right
            
        
        return dfs(root, 0, targetSum)
            