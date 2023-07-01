class Solution:
    def reorganizeString(self, s: str) -> str:
        
        frequency = Counter(s)
        heap = []
        
        for letter, count in frequency.items():
            heappush(heap, (-count, letter))
        
        ans = []
        while heap:
            if len(heap) > 1:
                count1, let1 = heappop(heap)
                count2, let2 = heappop(heap)
                
                if ans and ans[-1] == let1:
                    ans.append(let2)
                    ans.append(let1)
                
                else:
                    ans.append(let1)
                    ans.append(let2)
                
                if count1 < -1:
                    heappush(heap, (count1 + 1, let1))
                
                if count2 < -1:
                    heappush(heap, (count2 + 1, let2))
                
            
            else:
                count, let = heappop(heap)
                if ans and ans[-1] == let:
                    return ''
                
                ans.append(let)
                if count < -1:
                    heappush(heap, (count + 1, let))
        
        return ''.join(ans)
                

            