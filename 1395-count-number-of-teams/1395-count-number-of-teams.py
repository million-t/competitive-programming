class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        length = len(rating)
        count = 0
        
        for indx, middle in enumerate(rating):
            mins = [0, 0]
            maxes = [0, 0]
            for jindx, num in enumerate(rating):
                if num < middle:
                    mins[int(jindx > indx)] += 1
                
                if num > middle:
                    maxes[int(jindx > indx)] += 1
                    
            count += mins[0]*maxes[1] + mins[1]*maxes[0]
    
        return count