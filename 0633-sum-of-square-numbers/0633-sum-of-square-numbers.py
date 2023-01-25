class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        arr = range(int(c**(0.5)) + 1)
        
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            if arr[left]**2 + arr[right]**2 > c:
                right -= 1
            
            elif arr[left]**2 + arr[right]**2 < c:
                left += 1
            
            else:
                return True
        
        return False
                