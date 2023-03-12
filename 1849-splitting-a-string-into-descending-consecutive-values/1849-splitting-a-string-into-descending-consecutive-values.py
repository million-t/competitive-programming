class Solution:
    def splitString(self, s: str) -> bool:
        
        
        slices = []
        def backtrack(larger_slice):
            
            if not larger_slice:
                
                return True
            
            for index in range(1, len(larger_slice) + 1):
                
                new_slice = int(larger_slice[:index])
                if not slices or slices[-1] == new_slice + 1:
                    
                    slices.append(new_slice)
                    if backtrack(larger_slice[index:]) and len(slices) > 1:
                        return True
                    
                    slices.pop()
                    
            return False
        
        return backtrack(s)
            
        