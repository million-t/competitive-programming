from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        
        sorted_part = SortedList()
        cost = 0
        
        for num in instructions:
            cost += min(sorted_part.bisect_left(num), len(sorted_part) - sorted_part.bisect_right(num))
            sorted_part.add(num)
        
        return cost%(10**9 + 7)