class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        
        def char_bit(word):
            
            ord_a = ord('a')
            num = 0
            
            for char in word:
                ind = ord(char) - ord_a
                shift = 1<<ind
                num |= shift
            
            return num
        
        
        bit_set = [char_bit(word) for word in words]
        
        
        max_product = 0
        length = len(words)
        
        
        for first in range(length):
            
            
            for second in range(first + 1, length):
                
                if not bit_set[first] & bit_set[second]:
                    max_product = max(max_product, len(words[first])*len(words[second]))    
        
        
        return max_product