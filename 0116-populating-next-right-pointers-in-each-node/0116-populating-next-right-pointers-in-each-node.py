"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        store = {}
        
        def preorderDFS(cur, level):
            
            if not cur:
                return
            
            preorderDFS(cur.left, level + 1)
            if level in store:
                store[level].next = cur
            
            store[level] = cur
            preorderDFS(cur.right, level + 1)
        
        preorderDFS(root, 0)
        return root
        
        