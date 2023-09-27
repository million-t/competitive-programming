class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        
        dp = [0]
        end = 0
        
        for ind, char in enumerate(s):
            covered = dp[-1]
            
            if char.isnumeric():
                covered *= int(char)
            
            else:
                covered += 1
            
            dp.append(covered)
            if covered >= k:
                end = ind
                break
                
        
        def helper(ind, target):
            
            if dp[ind + 1] == target and not s[ind].isnumeric():
                return s[ind]
             
            
            if s[ind].isnumeric():
                mod = target%dp[ind]
                if not mod:
                    mod = dp[ind]
                return helper(ind - 1, mod)
            
            return helper(ind - 1, target)
                        
        
        
        return helper(end, k)
            
        