class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        
        nums.sort()
        target.sort()
        
        odds = []
        evens = []
        for num in nums:
            if num&1:
                odds.append(num)
            
            else:
                evens.append(num)
        
        oTar = []
        eTar = []
        for num in target:
            if num&1:
                oTar.append(num)
            
            else:
                eTar.append(num)
        
        ans = 0
        temp = []
        for num1, num2 in zip(oTar + eTar, odds + evens):
            ans += max(num1 - num2, 0)//2
            temp.append((num1, num2))

        return ans