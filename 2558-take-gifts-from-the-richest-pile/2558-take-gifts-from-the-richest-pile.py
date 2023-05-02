class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        minHeap = []
        
        for val in gifts:
            heapq.heappush(minHeap, -1*val)
            
        res = 0
        
        for _ in range(k):
            largest = -1*(heapq.heappop(minHeap))
            res +=  largest
            heapq.heappush(minHeap, -1*(int(largest**0.5)))
        
        return sum(minHeap)*-1