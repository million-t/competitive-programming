class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split(' ')
        n = len(s)
        
        maxLen = 0
        
        for word in s:
            maxLen = max(maxLen, len(word))
        
        for i in range(n):
            curLen = len(s[i])
            if curLen < maxLen:
                s[i] += (' '*(maxLen-curLen))
        
        ans = []
        for indx in range(maxLen):
            temp = []
            for j in range(n):
                temp.append(s[j][indx])
            while temp[-1] == ' ':
                temp.pop()
            ans.append(''.join(temp))
        
        return ans
                
            
        