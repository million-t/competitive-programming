class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        outputArray = [0]*len(nums)
        n=0
        for num in nums:
            outputArray[n] = temp.index(num)
            n+=1
        return outputArray
