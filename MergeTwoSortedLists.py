# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,None)
        cur =dummy
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    cur.next = list1
                    temp = list1.next
                    list1.next = list2
                    list1 = temp
                    cur = cur.next
                else:
                    cur.next = list2
                    temp = list2.next
                    list2.next = list1
                    list2 = temp
                    cur = cur.next
            elif list1:
                cur.next = list1
                break
            elif list2:
                cur.next = list2
                break
        return dummy.next
