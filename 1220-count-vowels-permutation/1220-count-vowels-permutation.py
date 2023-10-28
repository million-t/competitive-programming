class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        mod = 10**9 + 7
        dp = {
            'a': 1,
            'e': 1,
            'i': 1,
            'o': 1,
            'u': 1
        }
        
        
        for num in range(1, n):
            a, e, i, o, u = dp['a'], dp['e'], dp['i'], dp['o'], dp['u']
            dp['a'] = (e + i + u)%mod
            dp['e'] = (a + i)%mod
            dp['i'] = (e + o)%mod
            dp['o'] = i%mod
            dp['u'] = (o + i)%mod
        
        
        return sum(dp.values())%mod
            
            
        
        
        
        