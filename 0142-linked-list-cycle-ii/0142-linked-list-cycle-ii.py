# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        intersection = None

        #find the intersection of fast and slow if there is a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                intersection = fast
                break
        
        #intersection doesn't exist if there's no cycle
        while intersection and head != intersection:
            head = head.next
            intersection = intersection.next
        
        return intersection
        
