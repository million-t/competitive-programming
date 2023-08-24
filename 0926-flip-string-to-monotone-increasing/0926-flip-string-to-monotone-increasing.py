class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        preceding_ones = [0]
        succeding_zeros = [0]
        length = len(s)
        
        for bit in s:
            preceding_ones.append(preceding_ones[-1] + int(bit))
            
        for ind in range(length - 1, 0, -1):
            succeding_zeros.append(succeding_zeros[-1] + 1 - int(s[ind]))
        
        succeding_zeros.reverse()
        ans = length
        
        for ind in range(length):
            zeros_after = preceding_ones[ind]
            ones_before = succeding_zeros[ind]
            ans = min(ans, ones_before + zeros_after)
        
        return ans