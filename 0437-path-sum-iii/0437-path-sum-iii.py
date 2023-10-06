# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        
        seen = defaultdict(int)
        seen[0] += 1
        self.ans = 0
        
        def dfs(node, path_sum):
            if not node: 
                return
            
            path_sum += node.val
            self.ans += seen[path_sum - targetSum]
            
            seen[path_sum] += 1
            
            dfs(node.left, path_sum)
            dfs(node.right, path_sum)
            
            seen[path_sum] -= 1
        
        dfs(root, 0)
        return self.ans
        