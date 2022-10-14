class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def isArithmetic(start,end):
            arr = nums[start:end+1]
            arr.sort()
            if len(arr)<2: return False
            elif len(arr) == 2: return True
            else:
                d = arr[1] - arr[0]
                for i in range(2,len(arr)):
                    if arr[i]-arr[i-1]!= d:
                        return False
                return True
        ans = []
        for x,y in zip(l,r):
            ans.append(isArithmetic(x,y))
        return ans
