# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        #============ find depth ===============================
        def findDepth(node):
            if not node: return 0
            
            left = 1 + findDepth(node.left)
            right = 1 + findDepth(node.right)
            return max(left, right)
        
        
        depth = findDepth(root)
        
        #============ establish output array ====================
        res = [[] for _ in range(depth)]
        
        #============ traverse level ============================
        def levelTraverse(node, k):
            if node:
                res[k].append(node.val)
                
                levelTraverse(node.left, k + 1)
                levelTraverse(node.right, k + 1)
        
        levelTraverse(root, 0)
        
        return res