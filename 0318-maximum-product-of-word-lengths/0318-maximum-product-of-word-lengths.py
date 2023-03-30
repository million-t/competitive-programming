class Solution:
    def maxProduct(self, words: List[str]) -> int:
        _set = [list(set(word)) for word in words]
        
        def char_bit(word):
            
            ord_a = ord('a')
            num = 0
            
            for char in word:
                ind = ord(char) - ord_a
                shift = 1<<ind
                num |= shift
            
            return num
        
        
        def is_valid(word, num):
            
            ord_a = ord('a')
            
            for char in word:
                ind = ord(char) - ord_a
                shift = 1<<ind
                
                if num&shift:
                    return False
            
            return True

        
        
        max_product = 0
        length = len(words)
        
        def backtrack(index, candidates, seen):
            nonlocal length, max_product
            
            if len(candidates) >= 2:
                max_product = max(max_product, len(candidates[0])*len(candidates[1]))
                return
        
            
            for next_index in range(index, length):
                
                if is_valid(_set[next_index], seen):
                    
                    candidates.append(words[next_index])
                    
                    backtrack(index + 1, candidates, char_bit(_set[next_index]))
                    
                    candidates.pop()
                
        
        backtrack(0, [], 0)
        
        return max_product