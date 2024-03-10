class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        
        
        self.ans = 0
        
        def merge(one, two):
            merged = []
            oi = ti = 0
            l = r = 0
            
            while oi < len(one) and ti < len(two):
                if one[oi] <= two[ti]:
                    merged.append(one[oi])
                    oi += 1
                    
                else:
                    
                    while l < len(one) and (one[l][0] + valueDiff < two[ti][0] or one[l][1] + indexDiff < two[ti][1]):
                        l += 1
                    
                    while r < len(one) and (one[r][0] - valueDiff <= two[ti][0] or one[r][1] + indexDiff < two[ti][1]):
                        r += 1
                    
                    if l < r:
                        self.ans |= 1
                        
                    merged.append(two[ti])
                    ti += 1
            
            while oi < len(one):
                merged.append(one[oi])
                oi += 1
            
            while ti < len(two):
                while l < len(one) and (one[l][0] + valueDiff < two[ti][0] or one[l][1] + indexDiff < two[ti][1]):
                    l += 1

                while r < len(one) and (one[r][0] - valueDiff <= two[ti][0] or one[r][1] + indexDiff < two[ti][1]):
                    r += 1

                if l < r:
                    self.ans |= 1
                
                merged.append(two[ti])
                ti += 1
            
            return merged
            
        
        def sort(arr):
            if len(arr) == 1:
                return [arr[0]]
            
            left = arr[:len(arr)//2]            
            right = arr[len(arr)//2:]

            return merge(sort(left), sort(right))
        
        
        temp = [(num, indx) for indx, num in enumerate(nums)]
        sort(temp)
        return self.ans