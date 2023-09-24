class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        
        length = len(stones)
        dp = defaultdict(set)
        
        
        for indx in range(length - 2, -1, -1):
            num = stones[indx]
            dp[indx].add(stones[-1] - stones[indx])
            
            for sec_indx in range(indx + 1, length - 1):
                sec_num = stones[sec_indx]
                k = sec_num - num
                
                for dif in [k - 1, k, k + 1]:
                    if dif in dp[sec_indx]:
                        dp[indx].add(k)
        
        
        return 1 in dp[0]
        