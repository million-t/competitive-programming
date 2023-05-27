# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        
        def dfs(node, _max):
            if not node:
                return 0
            
            count = 0
            if node.val >= _max:
                count += 1
            
            count += dfs(node.left, max(node.val, _max))
            count += dfs(node.right, max(node.val, _max))
            return count
        
        return dfs(root, float('-inf'))
            
            
            