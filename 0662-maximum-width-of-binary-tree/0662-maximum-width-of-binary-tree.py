# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        queue = deque([(root, 0)])
        ans = 0
        
        while queue:
            _min = float('inf')
            _max = 0
            for _ in range(len(queue)):
                node, indx = queue.popleft()
                _min = min(_min, indx)
                _max = max(_max, indx)
                
                if node.left:
                    queue.append((node.left, 2*indx))
                
                if node.right:
                    queue.append((node.right, 2*indx + 1))
                                
            ans = max(ans, _max - _min + 1)
        
        return ans