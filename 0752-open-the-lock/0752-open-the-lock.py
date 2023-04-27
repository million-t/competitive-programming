class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        movements = [
            (1, 0, 0, 0),
            (-1, 0, 0, 0),
            (0, 1, 0, 0),
            (0, -1, 0, 0),
            (0, 0, 1, 0),
            (0, 0, -1, 0),
            (0, 0, 0, 1),
            (0, 0, 0, -1),
        ]
        
        target = tuple([int(dig) for dig in target])
        
        deadends_set = set()
        for deadend in deadends:
            deadends_set.add(tuple([int(dig) for dig in deadend]))
        
        if (0, 0, 0, 0) in deadends_set: 
            return -1
        
        queue = deque([(0, 0, 0, 0, 0)])
        visited = set([(0, 0, 0, 0)])
        
        
        
        while queue:
            w1, w2, w3, w4, moves = queue.popleft()
            
            if (w1, w2, w3, w4) == target:
                return moves
            
            for d1, d2, d3, d4 in movements:
                new_w1, new_w2, new_w3, new_w4 = (w1 + d1)%10, (w2 + d2)%10, (w3 + d3)%10, (w4 + d4)%10 
                
                if (new_w1, new_w2, new_w3, new_w4) not in visited and (new_w1, new_w2, new_w3, new_w4) not in deadends_set:
                    queue.append((new_w1, new_w2, new_w3, new_w4, moves + 1))
                    visited.add((new_w1, new_w2, new_w3, new_w4))
        
        return - 1