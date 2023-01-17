class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size = len(heights)
        
        for i in range(size):
            
            isSorted = True
            
            for j in range(size - i - 1):
                
                if heights[j] < heights[j + 1]:
                    isSorted = False
                    
                    names[j], names[j + 1] = names[j + 1], names[j]
                    heights[j], heights[j + 1] = heights[j + 1], heights[j]
            
            if isSorted:
                break
        
        return names