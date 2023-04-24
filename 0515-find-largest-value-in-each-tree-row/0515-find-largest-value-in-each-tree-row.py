# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        
        output = []
        def dfs(node, depth):
            if not node:
                return
            
            if len(output) <= depth:
                output.append(node.val)
            
            else:
                output[depth] = max(output[depth], node.val)
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return output
            
        