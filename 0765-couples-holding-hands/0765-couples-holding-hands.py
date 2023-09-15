class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        
        temp = []
        for num in row:
            temp.append(num//2)
        
        ind_memo = {}
        for ind, num in enumerate(temp):
            ind_memo[num] = ind
        
        
        swaps = 0
        for ind in range(1, len(temp), 2):
            sec_ind = ind_memo[temp[ind - 1]]
            if sec_ind != ind:
                cur = temp[ind]
                temp[ind], temp[sec_ind] = temp[sec_ind], temp[ind]
                ind_memo[cur] = max(ind_memo[cur], sec_ind)
                swaps += 1
            
            
        return swaps