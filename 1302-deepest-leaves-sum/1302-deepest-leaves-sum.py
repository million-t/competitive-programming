# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        
        queue = deque([root])
        res_sum = 0
        while queue:
            size = len(queue)
            
            _sum = 0
            for _ in range(size):
                cur = queue.popleft()
                _sum += cur.val
                
                if cur.left: 
                    queue.append(cur.left)
                
                if cur.right:
                    queue.append(cur.right)
                    
            res_sum = _sum
        
        return res_sum