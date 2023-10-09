# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        count = defaultdict(int)
        ans = []
        
        def dfs(node):
            
            if not node:
                return '_'
            
            left = dfs(node.left)
            right = dfs(node.right)
            cur_ans = '|' + str(node.val) + '|' + left + right
            count[cur_ans] += 1
            if count[cur_ans] == 2:
                ans.append(node)
            
            return cur_ans
        
        dfs(root)
        return ans

        