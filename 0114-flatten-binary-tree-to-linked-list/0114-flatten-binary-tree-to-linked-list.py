# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        
        def preorder(node):
            if not node:
                return None
            
            if node.left and node.right:
                startl, endl = preorder(node.left)
                startr, endr = preorder(node.right)
                endl.right = startr
                node.right = startl
                node.left = None
                return node, endr
                
            
            if node.left:
                startl, endl = preorder(node.left)
                node.right = startl
                node.left = None
                return node, endl
            
            elif node.right:
                startr, endr = preorder(node.right)
                node.right = startr
                node.left = None
                return node, endr
            
            else:
                return node, node
        
        preorder(root)
                
            
            