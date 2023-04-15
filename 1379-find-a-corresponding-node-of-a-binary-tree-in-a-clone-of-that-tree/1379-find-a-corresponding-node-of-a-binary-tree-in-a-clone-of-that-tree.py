# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def preorderDFS(node):
            
            if node:
                if node.val == target.val:
                    return node
                
                left = preorderDFS(node.left)
                right = preorderDFS(node.right)
                
                return left or right
        
        return preorderDFS(cloned)