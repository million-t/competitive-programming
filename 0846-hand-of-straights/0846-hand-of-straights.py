class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True
        
        groupSize = -groupSize
        hand.sort()
        heap = []
        
        for item in hand:
            if groupSize == 1:
                continue
                
            elif not heap:
                heappush(heap, (item, -1))
            
            elif heap[0][0] + 1 == item:
                prev_item, count = heappop(heap)
                
                count -= 1
                if count > groupSize:
                    heappush(heap, (item, count))
                
            elif heap[0][0] + 1 < item:
                return False
            
            else:
                heappush(heap, (item, -1))
                
        return not heap
                
        