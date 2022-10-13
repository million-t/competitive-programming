class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1]*len(nums1)
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                top = stack.pop()
                ans[nums1.index(top)] = num
            if num in nums1:
                stack.append(num)

        return ans
