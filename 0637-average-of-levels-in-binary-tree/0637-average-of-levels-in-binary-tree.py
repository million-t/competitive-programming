# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        
        sum_count = []
        queue = deque([(root, 1)])
        visited = set([root])
        
        while queue:
            cur, level = queue.popleft()
            
            if len(sum_count) < level:
                sum_count.append([cur.val, 1])
            
            else:
                sum_count[level - 1][0] += cur.val
                sum_count[level - 1][1] += 1
            
            if cur.left:
                queue.append((cur.left, level + 1))
            
            if cur.right:
                queue.append((cur.right, level + 1))
                
        
        averages = []
        for _sum, count in sum_count:
            averages.append(_sum/count)
        
        return averages
        