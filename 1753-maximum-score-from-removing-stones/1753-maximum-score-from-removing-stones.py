class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        heap = [-a, -b, -c]
        
        heapify(heap)
        ops = 0
        
        while len(heap) > 1:
            one = -heappop(heap)
            two = -heappop(heap)
            
            one -= 1
            two -= 1
            if one:
                heappush(heap, -one)
            
            if two:
                heappush(heap, -two)
            
            ops += 1
        
        return ops