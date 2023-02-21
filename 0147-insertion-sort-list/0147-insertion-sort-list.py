# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-5001)
        newNode = head
        
        while newNode:
            temp = newNode.next
            
            cur = dummy
            while cur and cur.next:
                
                if cur.next.val >= newNode.val:
                    break
                
                cur = cur.next
                
            another_temp = cur.next
            cur.next = newNode
            newNode.next = another_temp
            
            newNode = temp
            
        return dummy.next