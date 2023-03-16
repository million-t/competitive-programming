# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        #========================================
        def reverseNodes(left_node, right_node):
            
            prev = None
            cur = left_node
            
            while cur and prev != right_node:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur  = temp
                
            return prev, left_node
        #========================================
        
        left = right = head
        
        dummy = ListNode()
        cur = dummy
        while right:
            
            # find the next group boundary 
            i = 1
            while i < k and right.next:
                right = right.next
                i += 1
                
            #====================================
            
            if i == k:
                temp = right.next
            
                new_left, new_right = reverseNodes(left, right)
                cur.next = new_left
                cur = new_right
            
                left = right = temp
            
            else:
                cur.next = left
                break
                
        return dummy.next
            
            
                
        