# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        parent = {}
        queue = deque()
        
        def dfs1(node, par):
            if not node: return
            
            if node.val == start:
                queue.append(node)
                
            parent[node] = par
            dfs1(node.left, node)
            dfs1(node.right, node)
        
        dfs1(root, None)
        
        visited = set([start])
        level = -1
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                
                for neigh in [cur.left, cur.right, parent[cur]]:
                    if neigh and neigh.val not in visited:
                        visited.add(neigh.val)
                        queue.append(neigh)
                
            level += 1
            
        return level