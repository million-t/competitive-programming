class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        
        length = len(s)
        power_dp = [1]
        for num in range(k):
            power_dp.append((power_dp[-1]*power)%modulo)
        
        
        right = length - 1
        cur_hash = 0
        ans = (-1, -1)
        
        for left in range(length - 1, -1, -1):
            cur_hash *= power
            cur_hash += ord(s[left]) - ord('a') + 1
            cur_hash %= modulo
            
            if right - left + 1 == k:
                if cur_hash == hashValue:
                    ans = (left, right + 1)
                
                cur_hash -= (ord(s[right]) - ord('a') + 1)*power_dp[k - 1]
                cur_hash %= modulo
                right -= 1
        
        return s[ans[0]: ans[1]]
                
                
            
            
        