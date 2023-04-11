# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        
        
        def dfs(parent, grand_Parent):
            even_valued_grandparent = 0
            
            
            if parent.left:
                if not grand_Parent%2:
                    even_valued_grandparent += parent.left.val
            
                even_valued_grandparent += dfs(parent.left, parent.val)
            
            if parent.right:
                if not grand_Parent%2:
                    even_valued_grandparent += parent.right.val
                
                even_valued_grandparent += dfs(parent.right, parent.val)
            
            
            return even_valued_grandparent
        
        return dfs(root, 1)