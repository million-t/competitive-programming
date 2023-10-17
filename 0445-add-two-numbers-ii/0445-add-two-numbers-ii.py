# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(node):
            prev = None
            while node:
                next = node.next
                node.next = prev
                prev = node
                node = next
            
            return prev
        
        tail1 = reverse(l1)
        tail2 = reverse(l2)
        
        
        sum_tail = ListNode()
        cur = sum_tail
        carry = 0
        
        while tail1 or tail2:
            if tail1 and tail2:
                dig = tail1.val + tail2.val + carry
                carry = dig//10
                cur.val = dig%10
                cur.next = ListNode()
                cur = cur.next
                tail1 = tail1.next
                tail2 = tail2.next
            
            elif tail1:
                dig = tail1.val + carry
                carry = dig//10
                cur.val = dig%10
                cur.next = ListNode()
                cur = cur.next
                tail1 = tail1.next
            
            else:
                dig = tail2.val + carry
                carry = dig//10
                cur.val = dig%10
                cur.next = ListNode()
                cur = cur.next
                tail2 = tail2.next
        
        if carry:
            cur.val = carry
            cur.next = ListNode()
            cur = cur.next
        
        head_prev = reverse(sum_tail)
        return head_prev.next