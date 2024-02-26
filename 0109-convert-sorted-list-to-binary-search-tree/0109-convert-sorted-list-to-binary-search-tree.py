# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        
        def dc(head):
            
            if not head:
                return None
            
            if not head.next:
                return TreeNode(head.val)
            
            prev = None
            slow = head
            fast = head
            while fast and fast.next:
                fast = fast.next.next
                prev = slow
                slow = slow.next
        
            prev.next = None
            
            return TreeNode(slow.val, dc(head), dc(slow.next))
        
        return dc(head)