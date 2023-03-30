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
            
            for index, val in enumerate(nums):
                
                if not considered & 1<<index:
                    
                    considered ^= 1<<index
                    items.append(val)
                    
                    backtrack(items)
                    
                    items.pop()
                    considered ^= 1<<index
                    
        backtrack([])
        return permutations        
                