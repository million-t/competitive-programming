class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        srtd = sorted(nums)
        return nums == srtd or nums[::-1] == srtd