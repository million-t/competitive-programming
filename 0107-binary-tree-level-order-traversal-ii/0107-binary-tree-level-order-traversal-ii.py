# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        level_order = []
        
        def traverse(node, level):
            
            if node:
                if level >= len(level_order):
                    level_order.append([])
                
                level_order[level].append(node.val)
                
                traverse(node.left, level + 1)
                traverse(node.right, level + 1)
        
        traverse(root, 0)
        
        return level_order[::-1]
        