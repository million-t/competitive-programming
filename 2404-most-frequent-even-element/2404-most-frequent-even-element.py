class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums.sort()
        count = Counter(nums)
        
        maxOcur = 0
        evenNum = -1
        
        for num, c in count.items():
            if num%2==0 and c > maxOcur:
                evenNum = num
                maxOcur = c
        
        return evenNum
                