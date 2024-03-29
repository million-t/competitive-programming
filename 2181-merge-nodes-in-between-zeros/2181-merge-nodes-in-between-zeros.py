# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        
        run_sum = 0
        node = head.next
        
        while node:
            
            while node and node.val:
                run_sum += node.val
                node = node.next
            
            cur.next.val = run_sum
            cur = cur.next
            run_sum = 0
            
            if node:
                node = node.next
            
        
        cur.next = None
        return dummy.next