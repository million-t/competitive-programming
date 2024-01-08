class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        
        heap = []
        for left, right, height in buildings:
            heappush(heap, (left, -height, right))
        
        ans = []
        pr, ph = heap[0][0], 0
        
        while heap:
            left, neg_height, right = heappop(heap)
            
            if left < pr:
                if -neg_height > ph:
                    ans.append([left, -neg_height])
                    if pr > right:
                        heappush(heap, (right, -ph, pr))
                        
                    ph = -neg_height
                    pr = right
                    
                elif pr < right:
                    heappush(heap, (pr, neg_height, right))
                
            else:
                if left > pr:
                    ans.append([pr, 0])
                
                elif left == pr and ph == -neg_height:
                    pr = right
                    continue
                
                ans.append([left, -neg_height])
                ph = -neg_height
                pr = right
        
        ans.append([pr, 0])
        return ans
        