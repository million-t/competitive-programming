# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reversePointer(previous, current):
            if not current:
                return previous
            else:
                temp = current.next
                current.next = previous
                return reversePointer(current,temp)     
        return reversePointer(None,head)
