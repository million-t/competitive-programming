# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.ans = None
        
        
        def dfs(node):
            if self.ans or not node:
                return False
            
            
            left = dfs(node.left)
            right = dfs(node.right) 
            
            if left or right: 
                if left and right:
                    self.ans = node
                
                elif (left and (node == p or node == q)) or (right and (node == p or node == q)):
                    self.ans = node
                    
                return True
            
            return node == p or node == q
        
        dfs(root)
        return self.ans
        