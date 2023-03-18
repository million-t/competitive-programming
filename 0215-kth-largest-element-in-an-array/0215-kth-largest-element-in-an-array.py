class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        maxHeap = []
        
        for num in nums:
            heapq.heappush(maxHeap, -1*num)
        
        while k - 1:
            heapq.heappop(maxHeap)
            k -= 1
        
        return -1*maxHeap[0]
        
        