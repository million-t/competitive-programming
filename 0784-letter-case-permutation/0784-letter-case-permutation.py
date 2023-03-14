class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        length = len(s)
        
        variants = []
        
        def backtrack(cur_variant, index):
            
            if len(cur_variant) == length:
                variants.append(''.join(cur_variant))
                return
            
            
            for ind in range(index, length):
                
                char = s[ind]
                if char.isalpha():
                    
                    cur_variant.append(char.lower())
                    backtrack(cur_variant, ind + 1)
                    cur_variant.pop()
                    
                    cur_variant.append(char.upper())
                    backtrack(cur_variant, ind + 1)
                    cur_variant.pop()
                
                else:
                    cur_variant.append(char)
                    backtrack(cur_variant, ind + 1)
                    cur_variant.pop()
                    
        backtrack([], 0)
        
        return variants