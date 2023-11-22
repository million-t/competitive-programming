class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        
        diag = defaultdict(list)
        
        for row in range(len(nums)):
            for col in range(len(nums[row])):
                diag[row + col].append(nums[row][col])
        
        ans = []
        for d in diag:
            for val in diag[d][::-1]:
                ans.append(val)
        
        return ans