# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        _sum = 0        
        
        def traverse(node, path_sum):
            nonlocal _sum
            
            path_sum += str(node.val)

            if not (node.left or node.right):
                _sum += int(path_sum)
                return


            if node.left:
                traverse(node.left, path_sum)

            if node.right:
                traverse(node.right, path_sum)
        
        traverse(root, '')
        
        return _sum