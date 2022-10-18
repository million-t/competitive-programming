class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints)
        totSum, curWindowsum = sum(cardPoints), sum(cardPoints[: N-k ])
        curSum = curWindowsum
        left = 0
        for right in range(N-k, N):
            curSum = curSum -cardPoints[left] + cardPoints[right]
            curWindowsum = min(curWindowsum, curSum)
            left += 1
        return totSum - curWindowsum 
