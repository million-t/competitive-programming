class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        vals = Counter(arr).values()
        return len(set(vals)) == len(vals)