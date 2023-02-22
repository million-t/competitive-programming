class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        
        countS = {}
        countP = Counter(p)
        k = len(p)
        
        
        
        for i in range(k - 1):
            countS[s[i]] = countS.get(s[i], 0) + 1
        
        result = []
        left = 0
        
        for right in range(k - 1, len(s)):
            countS[s[right]] = countS.get(s[right], 0) + 1
            
            if countS == countP:
                result.append(left)
            
            countS[s[left]] = countS.get(s[left], 0) - 1
            
            if countS[s[left]] == 0:
                countS.pop(s[left])
            
            left += 1
        
        return result
        