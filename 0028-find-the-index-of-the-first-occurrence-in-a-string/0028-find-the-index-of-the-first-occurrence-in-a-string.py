class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        power = [1]
        
        for num in range(1, max(len(haystack), len(needle))):
            power.append(power[-1]*27)
        
        target = 0
        ord_a = ord('a')
        for indx, char in enumerate(needle[::-1]):
            target += (ord(char) - ord_a + 1)*power[indx]
        
        
        win_size = len(needle)
        left = 0
        cur_val = 0

        for right in range(len(haystack)):
            cur_val = cur_val*27 + (ord(haystack[right]) - ord_a + 1)
            
            
            if right - left + 1 == win_size:
                if cur_val == target:
                    return left
                
                cur_val -=  (ord(haystack[left]) - ord_a + 1)*power[win_size - 1]
                left += 1
        
        return -1
                
                
            
            
            