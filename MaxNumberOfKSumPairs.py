class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        #nums.sort()
        myDict, ans = {}, 0
        for num in nums:
            if k-num in myDict and myDict[k-num]>0:
                myDict[k-num]-=1
                ans+=1
            else:
                myDict[num] = 1 if num not in myDict else myDict[num] + 1
        return ans



