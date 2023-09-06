# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        size = 0
        cur = head
        while cur:
            cur = cur.next
            size += 1

        start = [None]*k
        
        mod = size%k
        quot = size//k
        
        if k > size:
            mod = 0
        ind = 0
        while head:
            cur  = head
            start[ind] = cur
            for num in range(quot - 1):
                cur = cur.next
            
            if mod and cur:
                cur = cur.next
                mod -= 1
              
            if cur:
                temp = cur.next
                cur.next = None
                head = temp
            
            else:
                head= cur
                
            ind += 1
            
        
        return start
        
        
        