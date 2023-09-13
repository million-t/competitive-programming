class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        temp = [1]*len(ratings)
        
        
        
        for ind in range(1, len(ratings)):
            if ratings[ind - 1] < ratings[ind]:
                temp[ind] = temp[ind - 1] + 1
        
        for ind in range(len(ratings) - 2, -1, -1):
            if ratings[ind + 1] < ratings[ind]:
                temp[ind] = max(temp[ind], temp[ind + 1] + 1)
        
        
        return sum(temp)