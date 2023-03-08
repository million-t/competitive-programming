# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        cur = root
        
        while cur:
            if p.val <= cur.val <= q.val or q.val <= cur.val <= p.val:
                return cur
            
            elif cur.val < p.val:
                cur = cur.right
            
            else:
                cur = cur.left
            
            
        return cur
            
        
        