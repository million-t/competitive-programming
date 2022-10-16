class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, ans = 0, len(height)-1, 0
        while left < right:
            ans = max(ans, (right-left)*min(height[left], height[right]))
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return ans
