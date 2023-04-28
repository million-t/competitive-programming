# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        myMap = {x: 0, y: 1}
        queue = deque([root])
        parents = {root.val: -1}
        
        while queue:
            size = len(queue)
            found = [0, 0]
            
            for _ in range(size):
                
                cur = queue.popleft()
                
                if cur.val in myMap:
                    found[myMap[cur.val]] = cur.val
                    
                if cur.left:
                    parents[cur.left.val] = cur
                    queue.append(cur.left)
                
                if cur.right:
                    parents[cur.right.val] = cur
                    queue.append(cur.right)
            
            if any(found):
                
                if all(found) and parents[found[0]] != parents[found[1]]:
                    return True
                
                return False
        
        return False