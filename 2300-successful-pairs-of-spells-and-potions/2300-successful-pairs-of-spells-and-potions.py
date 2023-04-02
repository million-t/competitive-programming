class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions.sort()
        successful = [0]*len(spells)
        
        for ind, spell in enumerate(spells):
            
            left = 0
            right = len(potions) - 1
            
            while left <= right:
                
                mid = left + (right - left)//2
                
                if potions[mid]*spell >= success:
                    right = mid - 1
                    
                else:
                    left = mid + 1
            
            successful[ind] = len(potions) - left
        
        return successful
                
        
        