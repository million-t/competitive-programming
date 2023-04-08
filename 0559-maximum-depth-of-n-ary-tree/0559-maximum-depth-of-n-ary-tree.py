"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        
        
        def dfs(node):
            
            
            if node:
                max_depth = 1
                
                for child in node.children:
                    
                    depth = dfs(child) + 1
                    max_depth = max(max_depth, depth)
                
                
                return max_depth
            
            return 0
        return dfs(root)