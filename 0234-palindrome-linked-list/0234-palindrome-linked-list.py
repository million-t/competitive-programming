# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def helper(n1, n2):
            if not n1:
                return True
            elif n1.val != n2.val:
                return False
            return helper(n1.next, n2.next)
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            cur = slow
            slow = slow.next
            fast = fast.next.next
            cur.next = prev
            prev = cur
        if fast:
            slow = slow.next
        return helper(slow, prev)


    def isPalindromeV1(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            cur = slow
            slow = slow.next
            fast = fast.next.next
            cur.next = prev
            prev = cur
        if fast:
            slow = slow.next
        while slow:
            if slow.val!=prev.val:
                return False
            slow = slow.next
            prev = prev.next
        return True 
        