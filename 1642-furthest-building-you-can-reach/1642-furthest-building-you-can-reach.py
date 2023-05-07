class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        heap = []
        prev = heights[0]
        
        
        for index in range(1, len(heights)):
            cur = heights[index]
            
            if cur > prev:
                
                change = cur - prev
                heappush(heap, change)
                
                pays = len(heap)
                if pays > ladders and heap[0] <= bricks:
                    minJump = heappop(heap)
                    bricks -= minJump
                
                elif pays > ladders:
                    return index - 1
                        
            prev = cur
            
        return len(heights) - 1
            