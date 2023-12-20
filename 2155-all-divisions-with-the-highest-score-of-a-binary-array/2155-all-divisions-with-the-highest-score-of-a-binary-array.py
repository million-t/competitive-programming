class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        zeros = [0]
        ones = [0]
        for indx in range(len(nums)):
            zeros.append(zeros[-1] +  1 - nums[indx])
            ones.append(ones[-1] + nums[~indx])
        
        ones.reverse()
        ans = []
        temp = []

        
        for indx in range(len(ones)):
            
            if temp and ones[indx] + zeros[indx] < temp[-1]:
                continue
            
            while temp and ones[indx] + zeros[indx] > temp[-1]:
                temp.pop()
                ans.pop()
            
            ans.append(indx)
            temp.append(ones[indx] + zeros[indx])
        
        return ans
                

    
        
        
        