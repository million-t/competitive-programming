# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        
        queue = deque([(root, 1)])
        
        while queue:
            
            cur_node, depth = queue.popleft()
            
            
            if cur_node.left or cur_node.right:
                
                if cur_node.left:
                    queue.append((cur_node.left, depth + 1))
                
                if cur_node.right:
                    queue.append((cur_node.right, depth + 1))
            
            else:
                return depth
        
        return 0
        