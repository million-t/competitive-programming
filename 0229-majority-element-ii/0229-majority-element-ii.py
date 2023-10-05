class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        target = len(nums)//3
        count = Counter(nums)
        ans = []
        
        for num, freq in count.items():
            if freq > target:
                ans.append(num)
        
        return ans
        