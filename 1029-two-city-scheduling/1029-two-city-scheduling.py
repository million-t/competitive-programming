class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        length = len(costs)
        
        dif_pair_map = {}
        cost_dif = []
        
        i = 0
        for a, b in costs:
            dif = a - b
            cost_dif.append((dif, i))
            dif_pair_map[(dif, i)] = a, b
            i += 1
            
        cost_dif.sort()
        
        min_cost = 0
        for index, (dif, i) in enumerate(cost_dif):    
            min_cost += dif_pair_map[(dif, i)][index >= length//2]
        
        return min_cost
        