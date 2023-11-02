class Solution:
    def numSplits(self, s: str) -> int:
        
        prefix = []
        count = set()
        
        for char in s:
            prefix.append(len(count))
            count.add(char)
        
        count = set()
        suffix = [0]*len(s)
        for indx in range(len(s) - 1, -1, -1):
            count.add(s[indx])
            suffix[indx] = len(count)
            
        
        ans = 0
        for indx in range(1, len(s)):
            if prefix[indx] == suffix[indx]:
                ans += 1
        
        return ans