# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next): return head
        
        prev = head
        cur = even = head.next
        
        i = 2
        while cur and cur.next:
            prev.next = cur.next
            prev = cur
            cur = cur.next
            i += 1
            
        if i%2: 
            cur.next = even
            prev.next = None
            
        else:
            prev.next = even
        
        return head