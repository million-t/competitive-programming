# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        hashmap = defaultdict(list)
        
        def traverse(node, level, x):
            if node:
                
                
                traverse(node.left, level + 1, x - 1)
                hashmap[x].append([level, node.val])
                traverse(node.right, level + 1, x + 1)
        
        traverse(root, 0, 0)
        
        res = []
        for key, lst in sorted(hashmap.items()):
            
            new = []
            for level, val in sorted(lst):
                new.append(val)
            
            res.append(new)
        
        return res