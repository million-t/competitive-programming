class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        ans = 0
        prev_max = 0
        
        for left, num in enumerate(arr):
            edge = left
            
            for right in range(len(arr) - 1, left - 1, -1):
                if arr[right] < num:
                    edge = right
                    break
            
            prev_max = max(edge, prev_max)
            if prev_max == left:
                ans += 1
        
        return ans
            