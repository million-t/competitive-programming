# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        

        max_sum = 0
        
        def postOrderTraverse(node):
            
            nonlocal max_sum
            
            if not node:
                return True, 0, float('inf'), float('-inf') 
            
            val = node.val
            
            left, left_sum, left_min, left_max = postOrderTraverse(node.left)
            right, right_sum, right_min, right_max = postOrderTraverse(node.right)
            
            if (left and right) and left_max < val < right_min:
                new_min = min(left_min, val)
                new_max = max(right_max, val)
                
                valid_sum = left_sum + right_sum + val
                max_sum = max(max_sum, valid_sum)
                
                return True, valid_sum, new_min, new_max
            
            
            return False, 0, 0, 0
            
            
            
            
        postOrderTraverse(root)
        
        return max_sum