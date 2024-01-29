class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        
        size = len(nums)
        pref = [[0]*size for num in range(size)]
        suf = [[0]*size for num in range(size)]
                
        for indx, num in enumerate(nums):
            for left in range(indx):
                if nums[left] < num:
                    pref[indx][left] += 1
                    suf[left][indx] += 1
        
        for row in range(size):
            for col in range(1, row):
                pref[row][col] += pref[row][col - 1]
            
            for col in range(size - 2, row, -1):
                suf[row][col] += suf[row][col + 1]
                

        ans = 0
        for right, num in enumerate(nums):
            for left in range(right):
                if num < nums[left]:
                    ans += pref[right][left]*suf[left][right]
                    
        return ans