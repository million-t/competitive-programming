# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next): return head
        
        odd = head
        temp = even = head.next
        cur = even.next
        i = 3
        
        while cur:
            
            if i%2:
                odd.next = cur
                odd = odd.next
                
            else:
                even.next = cur
                even = even.next
                
            cur = cur.next
            i += 1
            
        if even: even.next = None
            
        odd.next = temp

        return head