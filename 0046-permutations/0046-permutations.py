class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        max_length = len(nums)
        permutations = []
        
        considered = 0
        
        def backtrack(items):
            nonlocal considered
            
            if  len(items) == max_length:
                permutations.append(items[:])
                return
            
            shift = 1
            for index, val in enumerate(nums):
                
                if not considered & shift:
                    
                    considered ^= shift
                    items.append(val)
                    
                    backtrack(items)
                    
                    items.pop()
                    considered ^= shift
                
                shift = shift<<1
                    
        backtrack([])
        return permutations        
                