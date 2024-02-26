# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def dc(left, right):
            
            if left > right:
                return None
            
            mid = left + (right - left)//2
            cur = TreeNode(nums[mid])
            left = dc(left, mid - 1)
            right = dc(mid + 1, right)
            
            cur.left = left
            cur.right = right
            return cur
        
        return dc(0, len(nums) - 1)