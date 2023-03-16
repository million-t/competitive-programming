class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        length = len(ratings)
        candies = [1]*length
        
        for ind in range(1, length):
            
            if ratings[ind - 1] < ratings[ind]:
                candies[ind] = candies[ind - 1] + 1
                
                       
        for ind in range(length - 2, -1, -1):
            
            if ratings[ind + 1] < ratings[ind]:
                candies[ind] = max(candies[ind + 1] + 1, candies[ind])
          
        return sum(candies)
        