class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        arr = sorted([int(x) for x in nums], reverse=True)
        return str(arr[k-1])
