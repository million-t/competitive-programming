class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_ind = { char: ind for ind, char in enumerate(s) }
        
        
        substring_last = 0
        ans = []
        added_so_far = -1
        
        for ind, char in enumerate(s):
            substring_last = max(substring_last, last_ind[char])
            
            if substring_last == ind:
                
                ans.append(ind - added_so_far)
                added_so_far = ind
            
        
        return ans
        