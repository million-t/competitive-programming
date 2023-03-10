# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def mergeTwoLists(self, list1, list2):
        
        dummy = ListNode(0,None)
        cur = dummy
        
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
        
        
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not (head and head.next):
            return head
        
        slow = fast = head
        
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        secondHead = slow.next
        slow.next = None
        
        
        return self.mergeTwoLists(self.sortList(head), self.sortList(secondHead))
        
        
        