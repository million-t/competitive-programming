# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        levels = {}
        max_dif = 0
        
        def findWidth(node, level, x):
            nonlocal max_dif
            
            if node:
                if level not in levels:
                    levels[level] = [x, x]
                
                else:
                    
                    
                    levels[level][0] = min(levels[level][0], x)
                    levels[level][1] = max(levels[level][1], x)
                    
                max_dif = max(max_dif, levels[level][1] - levels[level][0] + 1)
                
                new_index = 2*x
                
                findWidth(node.left, level + 1, new_index)
                findWidth(node.right, level + 1, new_index + 1)
        
        findWidth(root, 0, 0)
        
        return max_dif