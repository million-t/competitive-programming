class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        
        queue = deque()
        max_arr = []
        
        left = 0
        for right, new_num in enumerate(nums):
            
            while queue and queue[-1] < new_num:
                queue.pop()
            
            queue.append(new_num)
            
            if right - left + 1 == k:
                max_arr.append(queue[0])
                
                if queue[0] == nums[left]:
                    queue.popleft()
                
                left += 1
        
        return max_arr
        