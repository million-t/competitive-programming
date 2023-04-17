class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        _max = max(candies)
        res = [False]*len(candies)
        
        for index, amount in enumerate(candies):
            if amount + extraCandies >= _max:
                res[index] = True
        
        return res
        
        