class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        
        mod = 10**9 + 7
        arr.sort()
        dp = defaultdict(int)

        
        for right, num1 in enumerate(arr):
            dp[num1] += 1
            
            for left in range(right + 1):
                num2 = arr[left]
                quot = num1/num2
                dp[num1] += (dp[quot]*dp[num2])%mod
                dp[num1] %= mod

        return sum(dp.values())%mod