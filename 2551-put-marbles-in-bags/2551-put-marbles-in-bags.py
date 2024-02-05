class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
    
        borders = []    
        for indx in range(1, len(weights)):
            borders.append(weights[indx] + weights[indx - 1])
        
        borders.sort()
        return sum(borders[len(borders) - k + 1:]) - sum(borders[:k - 1])
        
        