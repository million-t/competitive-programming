# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.indx = 0
        self.ans = -1
        
        def inorderDFS(node):
            
            if not node or self.ans != -1:
                return
            
            inorderDFS(node.left)
            self.indx += 1
            if self.indx == k:
                self.ans = node.val
                return 
            
            inorderDFS(node.right)
        
        inorderDFS(root)
        return self.ans
    
            