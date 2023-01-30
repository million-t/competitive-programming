# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummyGreater = ListNode()
        dummyLess = ListNode()
        curLess = dummyLess
        curGreater = dummyGreater
        
        while head:
            
            if head.val < x:
                curLess.next = head
                curLess = curLess.next
            
            else:
                curGreater.next = head
                curGreater = curGreater.next
                
            head = head.next
            
        curGreater.next = None
        curLess.next = dummyGreater.next
        
        return dummyLess.next
        
            
        
        