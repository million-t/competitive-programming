class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size = len(heights)
        
        for i in range(size - 1):
            
            minIndx = i
            minNum = heights[i]
            
            for j in range(i + 1 , size):
                
                if heights[j] > minNum:
                    minIndx = j
                    minNum = heights[j]
            
            heights[minIndx], heights[i] = heights[i], heights[minIndx]
            names[minIndx], names[i] = names[i], names[minIndx]
        
        return names