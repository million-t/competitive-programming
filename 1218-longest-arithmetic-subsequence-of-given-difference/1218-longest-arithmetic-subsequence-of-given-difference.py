class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        dif_map = defaultdict(int)
        
        for num in arr:
            dif_map[num] = max(dif_map[num], dif_map[num - difference] + 1)
        
        return max(dif_map.values())