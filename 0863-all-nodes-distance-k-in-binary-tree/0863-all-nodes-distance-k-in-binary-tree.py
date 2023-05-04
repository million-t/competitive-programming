# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        
        parent = {}
        
        def preorderDFS(node, target):
            
            if node.left:
                parent[node.left] = node
                preorderDFS(node.left, target)
            
            if node.right:
                parent[node.right] = node
                preorderDFS(node.right, target)
        
        
        parent[root] = None
        preorderDFS(root, target)

        
        res = []
        queue = deque([target])
        visited = set([target])
        level = 0
        
        while queue:
            
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                
                if level == k:
                    res.append(cur.val)
                    continue
                    
                if cur.left and cur.left not in visited:
                    visited.add(cur.left)
                    queue.append(cur.left)
                
                if cur.right and cur.right not in visited:
                    visited.add(cur.right)
                    queue.append(cur.right)
                
                if parent[cur] and parent[cur] not in visited:
                    visited.add(parent[cur])
                    queue.append(parent[cur])
            
            level += 1
        
        return res
                
                
                
            