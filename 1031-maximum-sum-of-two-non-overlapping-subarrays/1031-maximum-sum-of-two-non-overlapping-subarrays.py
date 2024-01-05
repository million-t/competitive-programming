class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        
        
        def hp(f, s):
            size = len(nums)
            pref = [0]*size
            suf = [0]*size

            _sum = left = 0

            for right, num in enumerate(nums):
                _sum += num

                if right - left + 1== f:
                    pref[right] = max(pref[right - 1], _sum)
                    _sum -= nums[left]
                    left += 1

            _sum = 0
            right = size - 1
            for left in range(size - 1, -1, -1):
                _sum += nums[left]

                if right - left + 1 == s:
                    suf[left] = max(_sum, suf[left + 1]) if left < size - 1 else _sum
                    _sum -= nums[right]
                    right -= 1

            ans = 0
            for indx in range(f, size - s + 1):
                ans = max(ans, pref[indx - 1] + suf[indx])

            return ans
        
        return max(hp(firstLen, secondLen), hp(secondLen, firstLen))