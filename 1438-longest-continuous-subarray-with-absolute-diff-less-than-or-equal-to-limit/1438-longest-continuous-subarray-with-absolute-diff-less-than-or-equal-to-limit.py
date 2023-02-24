class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_queue = deque()
        min_queue = deque()
        
        # max_len = 0
        left = 0
        for right in range(len(nums)):
            
            while max_queue and max_queue[-1] < nums[right]:
                max_queue.pop()
            
            while min_queue and min_queue[-1] > nums[right]:
                min_queue.pop()
            
            min_queue.append(nums[right])
            max_queue.append(nums[right])
            
            # if max_queue[0] - min_queue[0] <= limit:
            #     max_len = max(max_len, right - left + 1)
            
            if max_queue[0] - min_queue[0] > limit:
                
                if nums[left] == min_queue[0]:
                    min_queue.popleft()
                
                if nums[left] == max_queue[0]:
                    max_queue.popleft()
            
                left += 1
            
            
                
                        
        
        return len(nums) - left