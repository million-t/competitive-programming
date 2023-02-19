# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        nodes = []
        
        def helper(node):
            nonlocal nodes
            
            if node:
                helper(node.left)
                nodes.append(node.val)
                helper(node.right)
        
        helper(root)
        return nodes
                
        