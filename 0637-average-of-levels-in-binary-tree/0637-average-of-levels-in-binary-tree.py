# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        averages = []
        queue = deque([root])
        
        while queue:
            
            size = len(queue)
            total = 0
            
            for _ in range(size):
                cur = queue.popleft()
                total += cur.val
                
                if cur.left:
                    queue.append(cur.left)
                
                if cur.right:
                    queue.append(cur.right)
            
            averages.append(total/size)
        
        return averages