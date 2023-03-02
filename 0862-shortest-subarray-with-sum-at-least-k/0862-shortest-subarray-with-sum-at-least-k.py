class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        prefix_sum = 0
        queue = deque()
        min_len = float('inf')
        
        queue.append([0, 0])
        for right, num in enumerate(nums):
            prefix_sum += num
            
            while queue and queue[-1][0] >= prefix_sum:
                queue.pop()
            
            while queue and prefix_sum - queue[0][0] >= k:
                less, left = queue.popleft()
                min_len = min(min_len, right - left + 1 ) 
            
            queue.append([prefix_sum, right + 1])
        
        return min_len if min_len != float('inf') else -1
        