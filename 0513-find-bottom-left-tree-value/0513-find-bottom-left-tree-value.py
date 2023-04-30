# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        queue = deque([root])
        last_val = root.val
        
        while queue:
            size = len(queue)
            
            for _ in range(size):
                cur = queue.popleft()
                last_val = cur.val
                
                
                if cur.right:
                    queue.append(cur.right)
                    
                if cur.left:
                    queue.append(cur.left)
                
        return last_val      
                
                    
                
                
        