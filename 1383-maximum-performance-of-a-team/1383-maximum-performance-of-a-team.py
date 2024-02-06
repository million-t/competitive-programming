class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        mod = 10**9 + 7
        
        heap = []
        temp = sorted(zip(efficiency, speed), reverse=True)
        
        selected_sum = 0
        ans = 0
        
        for indx in range(n):
            e, v = temp[indx]
            selected_sum += v
            ans = max(ans, selected_sum*e)
            
            if indx < k - 1:
                heappush(heap, v)
                
            elif heap and heap[0] < v:
                selected_sum -= heappop(heap)
                heappush(heap, v)
            
            else:
                selected_sum -= v
            
        return ans%mod
        