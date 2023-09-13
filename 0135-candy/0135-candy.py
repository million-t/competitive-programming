class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        ratings.append(float('inf'))
        prev = float('inf')
        temp = [0]*len(ratings)
        
        for ind in range(len(ratings) - 1):
            if prev >= ratings[ind] <= ratings[ind + 1]:
                temp[ind] = 1
            
            prev = ratings[ind]
        
        for ind in range(1, len(ratings) - 1):
            if not temp[ind] and ratings[ind - 1] < ratings[ind]:
                temp[ind] = temp[ind - 1] + 1
        
        for ind in range(len(ratings) - 3, -1, -1):
            if temp[ind] != 1 and ratings[ind + 1] < ratings[ind]:
                temp[ind] = max(temp[ind], temp[ind + 1] + 1)
        
        
        return sum(temp)