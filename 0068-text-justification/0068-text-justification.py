class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        pref = [0]
        size = len(words) + 1
        for word in words:
            pref.append(pref[-1] + len(word))
        
        
        ans = []
        left, right = 0, 1
        
        while right < size:
            slots = 0
            while right + 1 < size and pref[right + 1] - pref[left] + slots + 1 <= maxWidth:
                slots += 1
                right += 1
            
            excess = maxWidth - (pref[right] - pref[left] + slots)
            
            if right + 1 == size:
                temp = " ".join(words[left:right]) + " "*excess
                ans.append(temp)
                
            
            elif not slots:
                ans.append(words[right - 1] + " "*excess)
            
            else:
                each = excess // slots
                lucky = excess % slots
                temp = [each + 1]*slots
                for slot in range(lucky):
                    temp[slot] += 1

                line = []
                for indx in range(left, right - 1):
                    words[indx] += " "*temp[indx - left]
                    line.append(words[indx])
                    
                line.append(words[right - 1])
                ans.append("".join(line))
                
            left = right
            right += 1
        
        return ans
