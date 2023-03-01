# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.dummy = ListNode()
        self.cur = self.dummy
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            self.cur.next = list2
            return self.dummy.next
        
        if not list2:
            self.cur.next = list1
            return self.dummy.next
        
        if list1.val < list2.val:
            self.cur.next = list1
            self.cur = list1
            return self.mergeTwoLists(list1.next, list2)
        
        self.cur.next = list2
        self.cur = list2
        return self.mergeTwoLists(list1, list2.next)
        