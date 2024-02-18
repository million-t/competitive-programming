class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        
        
        count = Counter()
        temp = [0]*len(s)
        max_count = 0
        
        for indx, char in enumerate(s):
            count[char] += 1
            temp[indx] = count[char] 
            max_count = max(max_count, count[char])
        
        
        ans = []
        for indx, char in enumerate(s):
            if temp[indx] == max_count:
                ans.append(char)
        
        
        return "".join(ans)