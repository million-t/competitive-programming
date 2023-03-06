class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #if len(citations) == 1: return 1 if citations[0] else 0
        
        length = len(citations)
        
        start = 0
        end = length - 1
        
        while start <= end:
            mid = start + (end - start)//2
            
            if citations[mid] < length - mid:
                start = mid + 1
                
            else:
                end = mid - 1
            
        return length - start
        