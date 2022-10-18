class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        res = []
        left, right = 0, len(p)-1
        countP,countS = Counter(p), Counter(s[left: right+1])
        while right<len(s):
            if countP == countS:
                res.append(left)
            if s[left] in countS.keys():
                if countS[s[left]] > 1:
                    countS[s[left]] -= 1
                else:
                    countS.pop(s[left])
                #countS[s[left]] -= 1 if countS[s[left]] > 1 else countS.pop(s[left]) 
            left+=1
            right+=1
            if right<len(s):
                countS[s[right]] += 1 if countS[s[right]] in countS.keys() else 1
        return res

            
