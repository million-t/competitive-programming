class Solution:
    def numberOfWays(self, s: str) -> int:
        
        bits = sum(map(int, s))
        pref_zeros, suf_zeros = 0, len(s) - bits
        pref_ones, suf_ones = 0, bits
        
        ans = 0
        for bit in s:
            if bit == '1':
                ans += pref_zeros*suf_zeros
                pref_ones += 1
                suf_ones -= 1
            else:
                ans += pref_ones*suf_ones
                pref_zeros += 1
                suf_zeros -= 1
        
        return ans
        
        
        