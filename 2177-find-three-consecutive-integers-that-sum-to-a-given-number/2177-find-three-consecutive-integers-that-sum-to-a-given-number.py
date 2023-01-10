class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        if num%3:
            return []
        
        factor = num//3
        return [factor - 1, factor, factor + 1]
        