# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        result = []
        stack = []
        i = 0
        
        while head:
            while stack and stack[-1][1] < head.val:
                result[stack.pop()[0]] = head.val
                
            stack.append([i, head.val])
            result.append(0)
            i += 1
            head = head.next
            
        return result
        
        '''
        N = 0
        cur1 = head
        while cur1:
            N+=1
            cur1 = cur1.next
        res = [0]*N
        stack = []
        i = 0
        while head:
            while stack and stack[-1][1] < head.val:
                res[stack.pop()[0]] = head.val
            stack.append([i, head.val])
            i += 1
            head = head.next
        return res'''
        