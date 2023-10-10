class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        
        temp = [a]
        pref = [0]*(len(b) + 2*len(a) )
        
        cur_size = len(a)
        
        while cur_size < len(b) + len(a):
            temp.append(a)
            pref[cur_size] = 1
            cur_size += len(a)
        
        for indx in range(1, len(pref)):
            pref[indx] += pref[indx - 1]
        
        
        template = "".join(temp)
        
        left = 0
        right = 1
        lps = [0]*len(b)
        
        while right < len(b):
            
            if b[right] == b[left]:
                lps[right] = left + 1
                left += 1
                right += 1
            
            elif not left:
                right += 1
            
            else:
                left = lps[left - 1]
        
        
        temp_indx = 0
        b_indx = 0
        b_len = len(b)
        ans = float('inf')
        
        while temp_indx < len(template):
            if b_indx < b_len and template[temp_indx] == b[b_indx]:
                b_indx += 1
                temp_indx += 1
            
            elif not b_indx:
                temp_indx += 1
            
            else:
                b_indx = lps[b_indx - 1]
                
            if b_indx == b_len:
                ans = min(ans, pref[temp_indx] - pref[temp_indx - b_len] + 1)
                
        
        return ans if ans != float('inf') else -1
        
        
        
        
        