class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        targetIndicesList = []
        for i in range(len(nums)):
            if nums[i] == target:
                targetIndicesList.append(i)
        return targetIndicesList
