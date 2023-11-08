class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        if maxK < minK:
            return 0
        
        minq = deque() 
        maxq = deque() 
        count = 0
        
        for indx, num in enumerate(nums):    
            
            min_indx = indx
            while minq and minq[-1][0] >= num:
                val, min_indx, i = minq.pop()
            
            max_indx = indx
            while maxq and maxq[-1][0] <= num:
                val, max_indx, i = maxq.pop()
            
            minq.append((num, min_indx, indx))
            maxq.append((num, max_indx, indx))
            
            while minq and minq[0][0] < minK:
                mn, mns, mni = minq.popleft()
                while maxq and maxq[0][2] <= mni:
                    maxq.popleft()
                
                if maxq and maxq[0][1] <= mni:
                    maxq[0][1] = mni + 1
            
            while maxq and maxq[0][0] > maxK:
                mx, mxs, mxi = maxq.popleft()
                while minq and minq[0][2] <= mxi:
                    minq.popleft()
                
                if minq and minq[0][1] <= mxi:
                    minq[0][1] = mxi + 1
                    
            plus = 0
            if minq and maxq and minq[0][0] == minK and maxq[0][0] == maxK:
                mn, mns, mni = minq[0]
                mx, mxs, mxi = maxq[0]
                plus = 1
                if mni < mxi:
                    count += mni - mns + 1
                
                elif mni > mxi:
                    count += mxi - mxs + 1
                    
                else:
                    count += min(mni - mns, mxi - mxs) + 1
            
            
        return count