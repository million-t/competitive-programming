class Solution:
    def maxLength(self, arr: List[str]) -> int:
        set_arr = [set(string) for string in arr]
        
        
        self.length = len(arr)
        self.max_length = 0
        
        def backtrack(_set, index, cur_len):
            self.max_length = max(self.max_length, cur_len)
            
            
            for i in range(index, self.length):
                
                new_elements = set_arr[i]
                new_len = len(new_elements)
                
                if new_len == len(arr[i]) and not _set.intersection(new_elements):
                        
                    _set = _set.union(new_elements)
                    backtrack( _set, i + 1, cur_len + new_len)
                    _set = _set.difference(new_elements)
                    
        backtrack(set(), 0, 0)
        
        return self.max_length