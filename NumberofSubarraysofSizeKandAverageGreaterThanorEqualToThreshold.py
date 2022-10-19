class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        targetSum = threshold*k    
        curSum = sum(arr[0:k])
        count = 1 if curSum >= targetSum else 0
        l = 0
        for r in range(k, len(arr)):
            curSum = curSum - arr[l] + arr[r]
            if curSum >= targetSum:
                count += 1
            l+=1
        return count


