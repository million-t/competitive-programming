# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        
        parent = {root: None}
        valid_leafs = []
        def dfs(node, path):
            
            path += node.val
            if (not node.left) and (not node.right):
                if path == targetSum:
                    valid_leafs.append(node)
                
                return
            
            if node.left:
                parent[node.left] = node 
                dfs(node.left, path)
            
            if node.right:
                parent[node.right] = node
                dfs(node.right, path)
            
        
        dfs(root, 0)
        ans = []
        for leaf in valid_leafs:
            
            temp = [leaf.val]
            while parent[leaf]:
                leaf = parent[leaf]
                temp.append(leaf.val)
            
            ans.append(temp[::-1])
        
        return ans