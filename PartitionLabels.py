class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {c:i for i,c in enumerate(s)}
        right, size = 0, 1
        ans = []
        for left, c in enumerate(s):
            right = max(right, lastIndex[c])
            if left == right:
                ans.append(size)
                size = 1
            else:
                size +=1
        return ans
