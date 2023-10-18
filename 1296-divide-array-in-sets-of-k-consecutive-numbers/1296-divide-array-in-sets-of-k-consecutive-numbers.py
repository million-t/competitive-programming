class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
        
        if k == 1:
            return True
        
        k = -k
        nums.sort()
        heap = []
        
        for item in nums:
            if k == 1:
                continue
                
            elif not heap:
                heappush(heap, (item, -1))
            
            elif heap[0][0] + 1 == item:
                prev_item, count = heappop(heap)
                
                count -= 1
                if count > k:
                    heappush(heap, (item, count))
                
            elif heap[0][0] + 1 < item:
                return False
            
            else:
                heappush(heap, (item, -1))
                
        return not heap
        