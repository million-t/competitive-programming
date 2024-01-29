class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        
        size = len(nums) + 1
        pref = [0]*size
        
        for indx, num in enumerate(nums):
            if num <= indx:
                pref[0] += 1
                pref[indx - num + 1] -= 1
                pref[indx + 1] += 1

            else:
                pref[indx + 1] += 1
                pref[size - (num - indx)] -= 1
        
        for indx in range(1, size):
            pref[indx] += pref[indx - 1]
        
        
        score = max(pref)
        for indx, count in enumerate(pref):
            if score == count:
                return indx
            
        