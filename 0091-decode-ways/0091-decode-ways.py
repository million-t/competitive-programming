class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        
        length = len(s)
        left = right = 0
        dp = [0]*(length + 2)
        dp[0] = dp[1] = 1
        ans = 1
        
        for num in range(2, length + 2):
            dp[num] = dp[num - 1] + dp[num - 2]
        
        while right < length:
            
            while right < length and (s[right] == '1' or s[right] == '2'):
                right += 1
            
            if right < length and s[right] == '0':
                
                if left >= right:
                    return 0
                
                left += 2
                right += 1
            
            elif right < length:
                if right > left and s[right - 1] == '2' and s[right] > '6':
                    pass
                
                else:
                    right += 1
            
            
            ans *= dp[right - left]
            left = right
        
        return ans
        
        