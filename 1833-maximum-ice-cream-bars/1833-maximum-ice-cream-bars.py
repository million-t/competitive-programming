class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs.sort()
        _sum = 0
        for indx, cost in enumerate(costs):
            _sum += cost
            if _sum > coins:
                return indx
        
        return len(costs)
        