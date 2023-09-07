# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        
        for i in range(1, left):
            cur = cur.next
            i += 1
        
        seg_1 = cur
        prev = cur
        
        cur = cur.next
        tail = cur
        for i in range(left, right):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            
        temp = cur.next
        cur.next = prev
        seg_1.next = cur
        
        tail.next = temp
        return dummy.next
        
            
            
            
            
            