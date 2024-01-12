class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        
        length = len(nums)
        right_flips = [0]*(length + k + 1)
        right = k
        left_flips = 0
        ans = 0
        
        for left, bit in enumerate(nums):
            bit ^= ((left_flips - right_flips[left]) & 1)
            
            if bit:
                right_flips[right] = right_flips[right - 1]
                
            else:
                if left > length - k:
                    return -1
                
                right_flips[right] = right_flips[right - 1] + 1
                
                left_flips += 1
                ans += 1
                
            right += 1
            
        return ans
            
                
        