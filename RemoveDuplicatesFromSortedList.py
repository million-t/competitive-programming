# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next): return head
        newHead = head 
        while head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            if head.next and head.val != head.next.val:
                head = head.next
        return newHead
