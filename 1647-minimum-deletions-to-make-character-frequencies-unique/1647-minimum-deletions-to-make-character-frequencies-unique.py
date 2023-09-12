class Solution:
    def minDeletions(self, s: str) -> int:
        
        count = Counter(s)
        temp = defaultdict(int)
        
        for char, freq in count.items():
            temp[freq] += 1
        
        removed = 0
        for num in range(max(temp), 0, -1):
            removed += max(temp[num] - 1, 0)
            temp[num - 1] += max(temp[num] - 1, 0)
        
        
        return removed
        