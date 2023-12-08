class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        
        seen = set()
        
        left = 0
        val = 0
        
        for right in range(len(s)):
            val *= 2
            val += int(s[right])
            
            if right - left + 1 == k:
                seen.add(val)
                val -= int(s[left])*(2**(right - left))
                left += 1
        
        return len(seen) == (2**k)