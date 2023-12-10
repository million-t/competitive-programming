class Solution:
    def findScore(self, nums: List[int]) -> int:

        marked = set()
        heap = []

        for indx, num in enumerate(nums):
            heappush(heap, (num, indx))
        
        score = 0
        while heap:
            cur_min, indx = heappop(heap)
            
            if indx in marked:
                continue
            
            score += cur_min
            marked.add(indx + 1)
            marked.add(indx - 1)
        
        return score