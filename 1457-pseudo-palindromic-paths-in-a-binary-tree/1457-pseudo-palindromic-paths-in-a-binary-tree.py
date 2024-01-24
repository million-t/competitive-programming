# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        
        
        def dfs(node, path):
            
            path[node.val] += 1
            
            ans = 0
            if not node.left and not node.right:
                
                odd = 0
                for num in path:
                    odd += num%2
                
                ans += odd < 2 
            
            if node.left:
                ans += dfs(node.left, path)
                
            if node.right:
                ans += dfs(node.right, path)
                
            path[node.val] -= 1
            return ans
        
        return dfs(root, [0]*10)