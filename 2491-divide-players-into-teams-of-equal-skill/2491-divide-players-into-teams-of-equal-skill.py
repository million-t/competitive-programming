class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        size = len(skill)
        
        chem = skill[0] + skill[-1]
        chem_sum = skill[0]*skill[-1]
        
        left, right = 1, size - 2
        
        while left < right:    
            if skill[left] + skill[right] != chem:
                return -1
            
            chem_sum += skill[left]*skill[right]
            
            left += 1
            right -= 1
            
        return chem_sum