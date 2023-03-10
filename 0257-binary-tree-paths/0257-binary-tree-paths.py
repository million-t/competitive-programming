# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        paths = []
        
        def backtrack(path, node):
            
            if  not (node.left or node.right):
                
                path.append(str(node.val))
                paths.append('->'.join(path))
                path.pop()
                
                return
            
            
            
            
            path.append(str(node.val))
                
            if node.left:
                backtrack(path, node.left)
            
            if node.right:
                backtrack(path, node.right)
                
            path.pop()
            
            
        
        backtrack([], root)
        
        return paths
        
            