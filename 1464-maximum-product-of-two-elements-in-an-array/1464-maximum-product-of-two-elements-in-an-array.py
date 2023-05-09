class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        heap = []
        for num in nums:
            heappush(heap, -num)

        num1 = -heappop(heap)
        num2 = -heappop(heap)
        
        return (num1 - 1)*(num2 - 1)