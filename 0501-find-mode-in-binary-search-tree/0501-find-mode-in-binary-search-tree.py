# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        count = defaultdict(int)
        
        def find_mode(node):
            if node:
                count[node.val] += 1
                
                find_mode(node.left)
                find_mode(node.right)
        
        find_mode(root)
        
        res = []
        
        for key, val in count.items():
            while res and count[res[-1]] < val:
                res.pop()
            
            if (not res) or (res and count[res[-1]] == val):
                res.append(key)
        
        return res