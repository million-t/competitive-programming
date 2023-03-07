# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        dummy = TreeNode(float('inf'), root)
        parent = dummy
        
        cur  = parent
        
        #===================== Search =================================
        while cur and cur.val != key:
            
            parent = cur
            
            if cur.val > key:
                cur = cur.left
                
            else:
                cur = cur.right
                
        #===================== Delete and Rearrange if found =================================
        if cur and not cur.left:
            
            if parent.left and parent.left.val == key:
                parent.left = cur.right
            
            else:
                parent.right = cur.right
            
            return dummy.left
        
        elif cur and not cur.right:
            if parent.left and parent.left.val == key:
                parent.left = cur.left
            
            else:
                parent.right = cur.left
            
            return dummy.left
        
        elif cur:
            if parent.left and parent.left.val == key:
                parent.left = cur.right
            
            else:
                parent.right = cur.right
                
            temp = cur.left
            cur = cur.right
            
            while cur.left:
                cur = cur.left
            
            cur.left = temp
        
        return dummy.left
            
        
        
        
        
        
        