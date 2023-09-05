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
        ind = 0
        while cur:
            _list[cur] = [ind, Node(cur.val)]
            cur = cur.next
            ind += 1
        
        
        for node in _list:
            ind, copy = _list[node]
            if node.random:
                copy.random = _list[node.random][1]
            if node.next:
                copy.next = _list[node.next][1]
        
        return _list[head][1]