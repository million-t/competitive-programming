class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        
        nums.sort()
        ans = []
        
        indx = 0
        
        while indx < len(nums):
            entry = []
            for _ in range(3):
                entry.append(nums[indx])
                indx += 1
            
            if entry[-1] - entry[0] > k:
                return []
            
            ans.append(entry)
        
        return ans