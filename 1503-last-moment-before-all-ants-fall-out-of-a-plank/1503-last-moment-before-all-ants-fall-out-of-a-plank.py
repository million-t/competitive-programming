class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        
        if left and right:
            max_left, min_right = max(left), min(right)
            return max(n - min_right, max_left)
        
        elif left:
            return max(left)
        
        else:
            return n - min(right)