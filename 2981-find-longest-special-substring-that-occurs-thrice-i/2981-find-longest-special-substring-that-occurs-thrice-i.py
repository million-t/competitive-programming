class Solution:
    def maximumLength(self, s: str) -> int:
        
        
        for ln in range(len(s) - 2, 0, -1):
            seen = defaultdict(int)
            
            for start in range(len(s) - ln + 1):
                temp = s[start:start + ln]
                if len(set(temp)) == 1:
                    seen[temp] += 1

                    if seen[temp] == 3:
                        return ln
                
        return -1