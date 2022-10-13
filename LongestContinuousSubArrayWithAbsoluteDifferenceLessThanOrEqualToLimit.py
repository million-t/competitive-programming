
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        largest = collections.deque()
        smallest = collections.deque()

        longest = 0
        left = 0
        for right,num in enumerate(nums):
            while len(largest)>0 and largest[-1] < num:
                largest.pop()
            largest.append(num)

            while len(smallest)>0 and smallest[-1]>num:
                smallest.pop()
            smallest.append(num)

            while largest[0] - smallest[0] > limit:
                if largest[0] == nums[left]:
                    largest.popleft()
                if smallest[0] == nums[left]:
                    smallest.popleft()
                left += 1
            longest = max(longest,right-left+1)
        return longest
