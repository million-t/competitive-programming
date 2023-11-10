class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        
        ans = []
        count = Counter(nums)
        
        for num, freq in count.items():
            if freq == 1 and num - 1 not in count and num + 1 not in count:
                ans.append(num)
                
        return ans