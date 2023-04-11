# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        _sum = 0        
        
        def dfs(node, path_sum):
            nonlocal _sum
            
            path_sum.append(str(node.val))

            if not (node.left or node.right):
                _sum += int(''.join(path_sum))
                path_sum.pop()
                return


            if node.left:
                dfs(node.left, path_sum)

            if node.right:
                dfs(node.right, path_sum)
            
            path_sum.pop()
            
        dfs(root, [])
        
        return _sum