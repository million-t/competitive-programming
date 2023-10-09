class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        gas_sum = sum(gas)
        cost_sum = sum(cost)
        
        if cost_sum > gas_sum:
            return -1
        
#         pref = [0]*len(gas)
#         for indx in range(len(gas)):
#             pref[indx] = max(pref[indx - 1] + gas[indx] - cost[indx], 0)
        
        ans = -1
        run_sum = 0
        indx = 0
        
        for cur_gas, cur_cost in zip(gas, cost):
            run_sum += cur_gas - cur_cost
            
            if run_sum < 0:
                ans = indx
                run_sum = 0
                
            indx += 1
        
        return (ans + 1)%len(gas)