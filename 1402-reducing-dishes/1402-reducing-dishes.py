class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        
        satisfaction.sort(reverse = True)
        max_coef = prev_val = 0
        prefix = 0
        
        for satisf in satisfaction:
            prev_val += prefix + satisf
            max_coef = max(max_coef, prev_val)
            prefix += satisf
            
        return max_coef