class Solution:
    def maxLength(self, arr: List[str]) -> int:
        set_arr = [set(string) for string in arr]
        
        _set = set()
        
        length = len(arr)
        max_length = 0
        def backtrack(index, cur_len):
            nonlocal max_length, length, _set
                
            max_length = max(max_length, cur_len)
            
            
            for i in range(index, length):
                
                new_elements = set_arr[i]
                new_len = len(new_elements)
                
                if new_len == len(arr[i]) and not _set.intersection(new_elements):
                        
                    _set = _set.union(new_elements)
                    backtrack(i + 1, cur_len + new_len)
                    _set = _set.difference(new_elements)
                    
        backtrack(0, 0)
        
        return max_length