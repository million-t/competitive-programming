# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not (head and head.next): return head 
        N = 0
        cur = head
        
        while cur:
            cur = cur.next
            N+=1
            
        k = k%N
        left = right = head
        
        while right and right.next:
            right = right.next
            if k:
                k-=1
            else:    
                left=left.next
                
        if not left.next: return head
        
        newHead = left.next
        right.next = head
        left.next = None
        
        return newHead



