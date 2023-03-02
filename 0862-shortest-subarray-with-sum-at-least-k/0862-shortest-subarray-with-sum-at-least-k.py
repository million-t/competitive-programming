class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        queue = deque()
        min_len = float('inf')
        
        for right, prefix in enumerate(prefix_sum):
            while queue and queue[-1][0] >= prefix:
                queue.pop()
            
            while queue and prefix - queue[0][0] >= k:
                less, left = queue.popleft()
                min_len = min(min_len, right - left)
            
            queue.append([prefix, right])
        
        return min_len if min_len != float('inf') else -1
        