class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        win_count = defaultdict(int)
        max_len = 0
        
        left = 0
        for right in range(len(fruits)):
            win_count[fruits[right]] += 1
            
            while len(win_count) > 2:
                win_count[fruits[left]] -= 1
                
                if not win_count[fruits[left]]:
                    win_count.pop(fruits[left])
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len
        