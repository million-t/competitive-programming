class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        mountLen = 0
        left = 0
        while left<len(arr):
            right = left + 1
            while right<len(arr) and arr[left] >= arr[right]:
                left+=1
                right+=1
            while right < len(arr)-1 and arr[right] < arr[right+1]:
                right += 1
            while right < len(arr)-1 and  arr[right] > arr[right+1]:
                right += 1
                curLen = right - left + 1
                mountLen = max(mountLen, curLen)
            left = right
        return mountLen

            
