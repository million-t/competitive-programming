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
        
        
        
        def is_valid(new_num, num):
            
            
            while new_num:
                if num&1 and new_num&1:
                    return False
                
                new_num >>= 1
                num >>= 1
                
                            
            return True
        
        
        
        max_product = 0
        length = len(words)
        
        
        for first in range(len(words)):
            
            
            for second in range(first + 1, len(words)):
                
                if is_valid(bit_set[second], bit_set[first]):
                    max_product = max(max_product, len(words[first])*len(words[second]))    
        
        
        return max_product