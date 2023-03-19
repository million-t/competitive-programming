class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        
        valid = [0, 0, 0]
        
        for triplet in triplets:
            first, second, third = triplet
            
            if first <= target[0] and second <= target[1] and third <= target[2]:
                
                for i in range(3):    
                    if triplet[i] == target[i]:
                        valid[i] = target[i]
                
        
        return all(valid)