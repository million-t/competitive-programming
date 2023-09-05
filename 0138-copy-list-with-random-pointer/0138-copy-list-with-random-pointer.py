"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        _list = {}
        
        cur = head
        while cur:
            _list[cur] = Node(cur.val)
            cur = cur.next
        
        
        for node in _list:
            copy = _list[node]
            
            if node.random:
                copy.random = _list[node.random]
            if node.next:
                copy.next = _list[node.next]
        
        return _list[head]