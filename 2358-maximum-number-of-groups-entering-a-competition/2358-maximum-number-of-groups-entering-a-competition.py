class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        
        grades.sort()
        _set = 0
        cur = 1
        
        while _set + cur <= len(grades):
            _set += cur
            cur += 1
        
        return cur - 1
        