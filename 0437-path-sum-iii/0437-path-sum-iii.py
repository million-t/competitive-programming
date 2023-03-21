# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        seen = defaultdict(int)
        valid_paths = 0
        seen[0] += 1
        
        def findPathSumEqualsK(cur_path_sum, node):
            nonlocal targetSum, valid_paths
            
            if node:
                
                cur_path_sum += node.val
                dif = cur_path_sum - targetSum
                valid_paths += seen[dif]
                
                
                seen[cur_path_sum] += 1
                
                findPathSumEqualsK(cur_path_sum, node.left)
                findPathSumEqualsK(cur_path_sum, node.right)
                
                seen[cur_path_sum] -= 1
                
        
        findPathSumEqualsK(0, root)
        
        return valid_paths
        