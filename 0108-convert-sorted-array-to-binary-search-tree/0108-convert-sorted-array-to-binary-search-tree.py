# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def dc(arr):
            
            if len(arr) == 0:
                return None
            
            if len(arr) == 1:
                return TreeNode(arr[0])
            
            mid = len(arr)//2
            cur = TreeNode(arr[mid])
            left = dc(arr[:mid])
            right = dc(arr[mid + 1:])
            
            cur.left = left
            cur.right = right
            return cur
        
        return dc(nums)