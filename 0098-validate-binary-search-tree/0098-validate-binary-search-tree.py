# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        prev = float('-inf')
        
        def inorder(node):
            nonlocal prev
            
            if node:
                left = inorder(node.left)
                
                if node.val > prev:
                    prev = node.val
                
                else:
                    return False
                
                right = inorder(node.right)
                
                return left and right
            
            return True
        
        
        return inorder(root)