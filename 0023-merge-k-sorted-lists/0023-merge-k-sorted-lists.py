# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = ListNode()
        cur = dummy
        
        heap = []
        for ind, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, ind))
        
        while heap:
            least, ind = heapq.heappop(heap)
            cur.next = lists[ind]
            cur = cur.next
            lists[ind] = lists[ind].next
            if lists[ind]:
                heapq.heappush(heap, (lists[ind].val, ind))
        
        cur.next = None
        
        return dummy.next
            
        