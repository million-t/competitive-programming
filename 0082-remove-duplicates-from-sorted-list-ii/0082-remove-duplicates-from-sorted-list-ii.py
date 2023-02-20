
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not (head and head.next): return head
        
        dummy = ListNode(None,head)
        curOut = dummy
        prev = dummy
        cur = head
        nxt = head.next
        
        while cur:
            temp = prev.next
            
            if nxt:
                
                if prev.val != cur.val != nxt.val:
                    curOut.next = cur
                    curOut = curOut.next
                    
                nxt = nxt.next

            else:
                if prev.val != cur.val:
                    
                    curOut.next = cur
                    curOut = curOut.next
                    
            prev = temp
            cur = cur.next
            
        curOut.next = None
        return dummy.next                     
                

