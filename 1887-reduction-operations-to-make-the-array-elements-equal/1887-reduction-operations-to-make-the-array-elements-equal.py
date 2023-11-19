class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        heap = []
        freq = Counter(nums)
        
        for num, count in freq.items():
            heappush(heap, (-num, count))
            
        ops = 0
        while len(heap) > 1:
            num1, c1 = heappop(heap)
            num2, c2 = heappop(heap)
            
            ops += c1
            heappush(heap, (num2, c2 + c1))
        
        return ops