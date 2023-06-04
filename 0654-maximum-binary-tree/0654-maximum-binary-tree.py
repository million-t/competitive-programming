# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        
        def build(start, end):
            
            _max_val = -1
            _max_ind = -1
            
            for index in range(start, end + 1):
                num = nums[index]
                if num > _max_val:
                    _max_val = num
                    _max_ind = index
            
            node = TreeNode(_max_val)
            
            if _max_ind > start:
                node.left = build(start, _max_ind - 1)
            
            if _max_ind < end:
                node.right = build(_max_ind + 1, end)
            
            return node
    
        return build(0, len(nums) - 1)
        