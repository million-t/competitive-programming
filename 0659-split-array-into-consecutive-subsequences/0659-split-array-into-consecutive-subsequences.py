class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        if len(set(nums)) < 3: 
            return False
        
        heap = []
        
        for num in nums:
            
            while heap and heap[0][0] < num - 1:
                tail, length = heappop(heap)    
                if length < 3:
                    return False
            
            if heap and heap[0][0] == num - 1:
                tail, length = heappop(heap)
                heappush(heap, (num, length + 1))
            
            else:
                heappush(heap, (num, 1))
            
            
        
        while heap:
            tail, length = heappop(heap)    
            if length < 3:
                return False
        
        return True
        
        
        
            