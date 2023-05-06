from heapq import heappush, heappop

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        heap = []
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                heappush(heap, matrix[row][col])
        
        
        ans = heap[0]
        while k:
            ans = heappop(heap)
            k -= 1
            
        
        return ans