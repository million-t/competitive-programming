# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carryOver = 0
        while l1 or l2 or carryOver:
            if l1 and l2:
                summ = l1.val + l2.val + carryOver
                l1, l2 = l1.next, l2.next
            elif l1:
                summ = l1.val + carryOver
                l1 = l1.next
            elif l2:
                summ = l2.val + carryOver
                l2 = l2.next
            elif carryOver:
                summ = carryOver
            
            if summ >= 10:
                newVal = summ%10
                carryOver = 1
            else:
                newVal = summ
                carryOver = 0
            newNode = ListNode(newVal, None)
            cur.next = newNode
            cur = cur.next  
        return dummy.next
