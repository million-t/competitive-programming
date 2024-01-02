class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        memo = defaultdict(list)
        count = defaultdict(int)
        
        for num in nums:
            count[num] += 1
            memo[count[num]].append(num)

        return list(memo.values())
        