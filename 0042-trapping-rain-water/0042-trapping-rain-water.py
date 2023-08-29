class Solution:
    def trap(self, height: List[int]) -> int:
        
        length = len(height)
        largest_before = [0]
        largest_after = [0]
        
        for ind in range(1, length):
            largest_before.append(max(largest_before[-1], height[ind - 1]))
        
        
        for ind in range(length - 2, -1, -1):
            largest_after.append(max(largest_after[-1], height[ind + 1]))
        
        largest_after.reverse()
        ans = 0
        
        for ind in range(length):
            ans += max(0, min(largest_before[ind], largest_after[ind]) - height[ind])
        
        return ans
        