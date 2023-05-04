class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        heap = []
        for pile in piles:
            heapq.heappush(heap, -1*pile)
        
        while k:
            cur_largest = heapq.heappop(heap)*-1
            heapq.heappush(heap, -1*ceil(cur_largest/2))
            k -= 1
        
        _sum = 0
        for num in heap:
            _sum -= num
            
        return _sum
            
        