class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        ans = []
        
        for indx in range(len(strs)):
            strs[indx] = sorted(strs[indx]), strs[indx]
        
        strs.sort()
        indx = 0
        
        while indx < len(strs):
            temp = ["".join(strs[indx][1])]
            while indx + 1 < len(strs) and strs[indx][0] == strs[indx + 1][0]:
                indx += 1
                temp.append("".join(strs[indx][1]))
            
            ans.append(temp)
            indx += 1
    
        
        return ans