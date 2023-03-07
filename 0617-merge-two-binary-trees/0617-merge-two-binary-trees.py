# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        new_root = None
        
        if root1 and root2:
            new_val = root1.val + root2.val
            new_root = TreeNode(new_val)
            
            new_root.left = self.mergeTrees(root1.left, root2.left)
            new_root.right = self.mergeTrees(root1.right, root2.right)
            
            
        
        elif root1:
        
            new_root = TreeNode(root1.val)
            
            new_root.left = self.mergeTrees(root1.left, None)
            new_root.right = self.mergeTrees(root1.right, None)
            
                    
        elif root2:
            
            new_root = TreeNode(root2.val)
            
            new_root.left = self.mergeTrees(None, root2.left)
            new_root.right = self.mergeTrees(None, root2.right)
            
        
        return new_root
            
            
            
        