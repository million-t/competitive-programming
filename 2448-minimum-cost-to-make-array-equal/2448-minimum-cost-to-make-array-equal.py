class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        temp = sorted([(num, c) for num, c in zip(nums, cost)])

        
        suf = []
        last = temp[-1][0]
        run_sum = 0
        costs = 0
        
        for indx, (num, cost) in enumerate(temp[::-1]):
            run_sum += costs*(last - num)
            suf.append(run_sum)
            costs += cost
            last = num
        
        suf.reverse()
        pref = []
        last = temp[0][0]
        run_sum = 0
        costs = 0
        
        for indx, (num, cost) in enumerate(temp):
            run_sum += costs*(num - last)
            pref.append(run_sum)
            costs += cost
            last = num
            
        ans = float('inf')
        for p, s in zip(pref, suf):
            ans = min(ans, p + s)
        
        return ans
        