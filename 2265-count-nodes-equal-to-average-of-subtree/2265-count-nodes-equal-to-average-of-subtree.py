# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        
        res = 0
        def findSumAndCount(node):
            nonlocal res
            
            if not node:
                return 0, 0
            
            left_sum, left_node_count = findSumAndCount(node.left)
            right_sum, right_node_count = findSumAndCount(node.right)
            
            new_sum = left_sum + right_sum + node.val
            new_count = left_node_count + right_node_count + 1
            
            if (new_sum)//(new_count) == node.val:
                res += 1
            
            return new_sum, new_count
        
        findSumAndCount(root)
            
        
        return res
        