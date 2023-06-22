class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        length = len(cost)
        cost.append(0)
        
        for ind in range(length - 3, -1, -1):
            cost[ind] += min(cost[ind + 1], cost[ind + 2])
    
        
        return min(cost[0], cost[1])
        